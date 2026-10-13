#!/usr/bin/env python3
"""Heuristic UI audit. Review findings and rendered output; exit 0 is not approval."""
import argparse
import json
import re
from pathlib import Path

SKIP = {'.git', 'node_modules', '.next', 'dist', 'build', 'coverage', '.expo', 'vendor', '__pycache__', 'playwright-report', 'test-results'}
EXT = {'.js', '.jsx', '.ts', '.tsx', '.mjs', '.cjs', '.css', '.scss', '.sass', '.less', '.html', '.vue', '.svelte', '.json'}
ALTERNATIVES = ('framer-motion', 'motion', '@react-spring/', 'react-spring', 'animejs', '@formkit/auto-animate', 'redux', '@reduxjs/toolkit', 'react-redux', 'jotai', 'recoil', 'mobx', 'mobx-react', 'valtio')
REQUIRED = {'Tabler': ('@tabler/',), 'React Aria / Spectrum': ('react-aria-components', '@adobe/react-spectrum', '@react-spectrum/'), 'GSAP': ('gsap',), 'Playwright': ('@playwright/test', 'playwright'), 'Zod': ('zod',), 'Zustand': ('zustand',)}
RULES = [
    ('review', 'tracking', r'\btracking-[\w\[.-]+|\bletter-spacing\s*:|\bletterSpacing\s*:', 'Conferir evidência registrada na referência.'),
    ('review', 'em-dash', '\u2014', 'Proibido se fizer parte de texto da interface.'),
    ('review', 'css-motion', r'\b(?:animation|transition)(?:-[\w-]+)?\s*:|\b(?:animation|transition)[A-Z]\w*\s*:|@(?:-webkit-)?keyframes\b|\b(?:animate|transition|duration|delay|ease)-[\w\[]+', 'Conferir efeito CSS incompatível com GSAP, inclusive estilos inline.'),
    ('review', 'web-animations', r'\.animate\s*\(', 'Verificar se é Web Animations API substituindo GSAP.'),
    ('review', 'context-state', r'\b(?:createContext|useContext|useReducer)\s*(?:<[^>]+>)?\s*\(', 'Conferir se substitui Zustand como estado global da aplicação.'),
    ('review', 'shadcn-origin', r'shadcn|ui\.shadcn\.com|@/components/ui/', 'Investigar origem; caminho components/ui não prova shadcn.'),
    ('review', 'border', r'\bborder(?:-[\w\[.#/-]+)?\b|\bborder[A-Z]\w*\s*:', 'Verificar uso visual e suporte específico na referência.'),
]
IMPORTS = re.compile(r'''(?:\bfrom\s*|\bimport\s*(?:\(\s*)?|\brequire\s*\(\s*)["']([^"']+)["']''')

def forbidden(package):
    if package == 'lucide' or package.startswith(('lucide-', '@lucide/')):
        return 'lucide'
    if package in ('shadcn', 'shadcn-ui') or package.startswith(('@shadcn/', 'shadcn/')):
        return 'shadcn'
    if any(package == x or package.startswith(x if x.endswith('/') else x + '/') for x in ALTERNATIVES):
        return 'alternative-library'
    return None

def audit(root, scopes):
    findings, manifests, uses = [], {}, {}
    count = 0
    def add(level, rule, path, line, evidence, reason):
        findings.append(dict(level=level, rule=rule, path=str(path.relative_to(root)), line=line, evidence=evidence[:220], reason=reason))
    selected = set()
    for scope in scopes or ['.']:
        base = (root / scope).resolve()
        if not base.is_relative_to(root) or not base.exists():
            raise ValueError('Escopo inexistente ou fora do projeto: ' + scope)
        for file in ([base] if base.is_file() else base.rglob('*')):
            if file.is_symlink() or not file.is_file() or any(x in SKIP for x in file.relative_to(root).parts):
                continue
            if file.suffix in EXT and not file.name.endswith(('.min.js', '.min.css', '.d.ts')) and file.name not in {'package-lock.json', 'bun.lock', 'pnpm-lock.yaml'}:
                selected.add(file)
    for file in sorted(selected):
        count += 1
        content = file.read_text(encoding='utf-8')
        if file.name == 'package.json':
            data = json.loads(content)
            for group in ('dependencies', 'devDependencies', 'peerDependencies', 'optionalDependencies'):
                for pkg, value in data.get(group, {}).items():
                    manifests.setdefault(pkg, []).append(str(file.relative_to(root)))
                    rule = forbidden(pkg)
                    if not rule and isinstance(value, str) and value.startswith('npm:'):
                        rule = forbidden(value[4:].rsplit('@', 1)[0])
                    if rule:
                        level = 'review' if rule == 'alternative-library' else 'violation'
                        add(level, rule, file, 1, pkg, 'Dependência proibida.' if level == 'violation' else 'Verificar uso alternativo para movimento ou estado global.')
        for match in IMPORTS.finditer(content):
            pkg = match.group(1)
            uses.setdefault(pkg, []).append(str(file.relative_to(root)))
            rule = forbidden(pkg)
            if rule:
                add('review', rule + '-source', file, content.count('\n', 0, match.start()) + 1, match.group(0), 'Conferir import executável e uso no escopo; comentários podem produzir falsos positivos.')
        for number, line in enumerate(content.splitlines(), 1):
            for level, rule, pattern, reason in RULES:
                if re.search(pattern, line):
                    add(level, rule, file, number, line.strip(), reason)
    if count == 0:
        raise ValueError('Nenhum arquivo suportado no escopo; auditoria não executada.')
    evidence = {}
    for label, prefixes in REQUIRED.items():
        evidence[label] = {kind: {pkg: paths for pkg, paths in entries.items() if any(pkg == prefix or pkg.startswith(prefix if prefix.endswith('/') else prefix + '/') for prefix in prefixes)} for kind, entries in [('dependencies', manifests), ('source_candidates', uses)]}
    return dict(files_scanned=count, scopes=scopes or ['.'], findings=findings, stack_evidence=evidence, note='Ausência de achados não comprova conformidade. Revisar origem, implementação, critérios aplicáveis, screenshots e Playwright.')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--scope', action='append', help='Caminho relativo autorizado; pode repetir.')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        if not root.is_dir():
            raise ValueError('Raiz precisa ser um diretório existente.')
        report = audit(root, args.scope)
    except (OSError, ValueError, UnicodeError) as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False))
        return 2
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Arquivos verificados: {report['files_scanned']}")
        for finding in report['findings']:
            print(f"{finding['level'].upper()} {finding['path']}:{finding['line']} [{finding['rule']}] {finding['reason']}")
        print('Evidências da stack (exigem revisão de implementação):')
        print(json.dumps(report['stack_evidence'], ensure_ascii=False, indent=2))
        print(report['note'])
    return 1 if any(x['level'] == 'violation' for x in report['findings']) else 0

if __name__ == '__main__':
    raise SystemExit(main())
