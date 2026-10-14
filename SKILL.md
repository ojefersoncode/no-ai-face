---
name: no-ai-face
description: Criar e redesenhar sites e interfaces com identidade visual própria, eliminando aparência genérica de IA. Usar ao desenvolver interfaces a partir de referências, aplicar novo branding, criar sites ou aplicações, ou quando o usuário pedir NO AI FACE. Exigir referência visual inspecionável antes da implementação e aplicar Tabler, React Aria ou Spectrum, GSAP, Playwright, Zod e Zustand conforme os requisitos aplicáveis.
---

# NO AI FACE

Ler [regras obrigatórias](references/regras.md) integralmente antes de agir. Tratar todos os requisitos como critérios de aceitação. Não flexibilizar obrigações nem substituir ferramentas por conveniência. Respeitar instruções superiores e orientações explícitas do usuário; não criar exceções por iniciativa própria.

## Executar o fluxo

Aplicar a [preservação visual estrita](references/regras.md#preservação-visual-estrita) em todas as etapas: preservar composição, proporções, densidade, arredondamentos, bordas e hierarquia da referência. Branding próprio permite adaptar nome, marca e conteúdo; não autoriza modificar essas características. Apresentar qualquer divergência visual ao usuário antes da implementação. Se a validação visual estiver bloqueada, parar as alterações visuais e informar o bloqueio.

**PARADA OBRIGATÓRIA:** cumprir o [protocolo de bloqueio da validação visual](references/regras.md#protocolo-de-bloqueio-da-validação-visual) antes da primeira alteração visual e sempre que servidor, navegador, captura ou abertura de screenshots falhar. Durante o bloqueio, trabalhar somente no diagnóstico e no reparo necessário à validação; fornecer comandos concretos ao usuário quando depender dele. Não continuar a interface nem declarar conclusão com uma ressalva de teste pendente. Retomar apenas com evidência real de servidor acessível, página correta renderizada no Playwright e screenshot atual aberta e inspecionada.

1. Verificar se o usuário forneceu referência visual acessível. Aceitar screenshot, imagem, arquivo de design ou URL que possa ser inspecionada visualmente. Reutilizar material já fornecido. Sem referência, solicitar e aguardar antes de implementar a interface. Uma descrição estética não substitui a referência. Declarar falhas de acesso sem inventar análise.
2. Se a referência for uma URL, seguir a [inspeção obrigatória por navegador](references/regras.md#inspeção-obrigatória-de-referências-por-url): tentar abri-la com Playwright em desktop e mobile, percorrer conteúdo e estados, capturar e **abrir as screenshots antes de implementar**. Verificar e, se necessário, instalar Playwright e seu Chromium no projeto. Registrar comandos, URLs, viewports e caminhos das capturas. Se a navegação ou captura falhar, registrar o erro concreto, solicitar um arquivo visual ao usuário e aguardar antes da implementação visual.
3. Inspecionar a referência. Registrar composição, hierarquia, tipografia, pesos, paleta, contraste, espaçamento, densidade, bordas, ícones e imagens. Distinguir comportamento responsivo observado de decisões propostas.
4. **Antes de implementar, inventariar todos os elementos visíveis e estados da referência**, incluindo navegação, busca, botões, formulários e menus. Para cada item, registrar onde será implementado e o comportamento previsto. Não omitir um controle por falta de backend: preservar sua presença visual e declarar o comportamento pendente, sem inventar um serviço.
5. Criar branding próprio baseado na linguagem visual observada, sem copiar nome, logo, textos ou elementos exclusivos da marca. Definir tokens. Registrar exatamente quais elementos justificam bordas e tracking; uma borda em um elemento não autoriza bordas em todos.
6. Inspecionar projeto, dependências e componentes no escopo. Identificar Lucide, shadcn/ui e conflitos com a stack. Corrigir dentro do escopo autorizado; se cumprir as regras exigir alterações fora dele, informar o impedimento e solicitar orientação antes da parte afetada. Aplicar o mesmo procedimento se a plataforma não suportar a stack exigida, inclusive apps nativos. Não trocar a stack silenciosamente.
7. Implementar a composição mobile primeiro e expandir para tablet e desktop. Usar Tabler e React Aria Components ou Adobe React Spectrum. Usar GSAP para animações e transições, incluindo respeito a movimento reduzido. Usar Zod em formulários e entradas do backend; registrar ausência de backend sem inventar um. Usar Zustand quando houver estado global; manter estado local local, sem inventar estado global.
8. Aplicar as regras visuais e de conteúdo. Proibir eyebrows, enumeração decorativa, travessões na interface e headers de tela com título mais descrição. Usar contraste por cores sólidas. Exigir evidência da referência para bordas e tracking. Remover descrições redundantes de cards. Registrar justificativa funcional para descrições necessárias e incluir descrições relevantes em cards de produtos de e-commerce. Preservar labels, unidades, legendas e erros necessários.
9. Executar o verificador estático abaixo. Revisar cada ocorrência no contexto e verificar pontos reais de uso da stack. Não confundir dependência instalada com requisito cumprido.
10. Executar [auditoria e Playwright](references/auditoria.md). Capturar e abrir screenshots; corrigir problemas e repetir as verificações afetadas. Usar [exemplos de decisões](references/exemplos.md) para interpretar situações recorrentes.
11. **Antes da entrega, comparar cada item e estado do inventário com a interface implementada**, verificar sua presença e localização e justificar toda diferença. Corrigir omissões não justificadas. Entregar o inventário reconciliado junto da referência utilizada, identidade criada, requisitos verificados, testes e resultados reais, screenshots inspecionadas e impedimentos. Só declarar conclusão após todos os critérios aplicáveis passarem. Identificar verificações não executadas como pendentes.

## Executar a análise estática

Resolver o caminho deste script a partir da pasta desta skill:

```bash
python <pasta-da-skill>/scripts/audit.py <raiz-do-projeto>
python <pasta-da-skill>/scripts/audit.py <raiz-do-projeto> --json
```

Usar `--scope src --scope package.json` para limitar a auditoria ao escopo autorizado quando necessário. Registrar os caminhos incluídos e os excluídos, sem reduzir o escopo para ocultar violações. Auditar pacotes e manifests relevantes em monorepos.

Interpretar códigos de saída: `0` sem violações confirmadas pelo scanner (pode haver revisão pendente); `1` violações detectadas; `2` erro de execução. Tratar todas as ocorrências `review` como pendências até verificá-las. O script usa heurísticas, não análise completa de AST ou de pixels: não prova origem de componentes copiados sem marcadores, não distingue todos os comentários de código e não detecta todas as formas de gerar estilos. Concluir somente após auditoria manual, visual e de interações.
