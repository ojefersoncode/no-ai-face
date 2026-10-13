# NO AI FACE

Skill para criar e redesenhar interfaces com identidade visual própria a partir de uma referência visual inspecionável.

## Conteúdo

- `SKILL.md`: instruções e fluxo de trabalho da skill.
- `references/regras.md`: requisitos de implementação e de linguagem visual.
- `references/auditoria.md`: verificações manuais e com Playwright.
- `references/exemplos.md`: exemplos de decisões recorrentes.
- `scripts/audit.py`: verificador estático para projetos de interface.
- `agents/openai.yaml`: metadados de apresentação.

## Auditoria estática

```bash
python3 scripts/audit.py /caminho/do/projeto
python3 scripts/audit.py /caminho/do/projeto --json
```

O verificador usa heurísticas. A auditoria visual e de interações descrita em `references/auditoria.md` também é necessária.
