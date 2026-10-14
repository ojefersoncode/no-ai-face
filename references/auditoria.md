# Auditoria técnica e visual

## Registro antes da implementação

Registrar no contexto de trabalho ou documentação do projeto: referência inspecionada; características observadas; inventário de todos os elementos visíveis e estados, com destino de implementação e comportamento previsto para cada item; decisões de branding e tokens; evidência específica para cada tratamento de borda e tracking; justificativa funcional de descrições excepcionais; escopo e incompatibilidades. Incluir navegação, busca, botões, formulários e menus. Não afirmar ter observado estados ou versões responsivas que não foram fornecidos. Se faltar backend, manter o controle visível e marcar seu comportamento como pendente, sem criar serviço fictício.

## Verificação estática e técnica

- Executar `scripts/audit.py` conforme SKILL.md. Revisar evidências, inclusive comentários e código não executado. Não descartar achados sem justificativa registrada.
- Verificar ausência de imports, dependências e ícones copiados de Lucide no escopo.
- Procurar componentes shadcn copiados/gerados, mesmo sem dependência ou marcador. Revisar origem dos componentes; Radix ou `components/ui` isoladamente não comprovam shadcn.
- Verificar Tabler nos ícones e React Aria Components ou Adobe Spectrum nos componentes interativos.
- Conferir GSAP nos pontos de animação e transição; procurar também estilos inline, CSS-in-JS e chamadas de Web Animations API. Não aceitar CSS transitions/animations como alternativa.
- Conferir Zod nos formulários e no backend que recebe dados. Verificar que entradas inválidas são rejeitadas no servidor, não só no cliente. Registrar quando backend ou formulário não existe no escopo.
- Conferir Zustand nos pontos de estado global. Distinguir contextos internos das bibliotecas de uso de Context API como substituto do estado global da aplicação.
- Conferir que ausência de movimento ou estado global não foi preenchida com efeitos ou estados artificiais.

## Testar com Playwright

Usar a configuração e os comandos existentes do projeto. Se não houver configuração, criar testes no projeto com Playwright, baseURL do servidor de desenvolvimento e navegadores disponíveis; conferir documentação oficial quando houver dúvida de API. Não inventar resultados quando o ambiente impedir a execução.

1. Abrir cada rota alterada em viewport mobile (por exemplo 390 x 844), tablet (768 x 1024) e desktop (1440 x 900). Incluir largura menor quando o conteúdo exigir. Avaliar mobile first também no código, não apenas no resultado de um breakpoint.
2. Testar fluxos principais, navegação por teclado, foco visível, formulários válidos e inválidos, menus e dialogs. Verificar fechamento, retorno de foco e acesso por toque quando aplicável.
3. Verificar overflow horizontal comparando scrollWidth e clientWidth, legibilidade, controles alcançáveis, reorganização de grids e conteúdo sem corte ou sobreposição. Um teste de largura não comprova todos esses itens.
4. Emular reducedMotion: reduce; verificar redução ou desativação dos efeitos GSAP. Limpar timelines e listeners ao desmontar componentes conforme o framework.
5. Capturar screenshots com `page.screenshot({path: ..., fullPage: true})` após carregar fontes, imagens e conteúdo. Abrir e inspecionar cada captura, incluindo estados relevantes de erro, menu e dialog.
6. Verificar ausência de eyebrows, números decorativos, headers com descrição, descrições redundantes, bordas não justificadas e contraste dependente de transparência/gradiente. Comparar com a referência e o registro de identidade, sem exigir cópia literal da marca.
7. Corrigir os problemas e repetir testes e capturas afetados. Não usar atualização de snapshots como prova de correção.

## Reconciliar o inventário antes da entrega

Comparar cada elemento e estado inventariado com a interface implementada e as screenshots. Registrar onde ficou, qual comportamento foi verificado e cada diferença em relação à referência, com justificativa. Corrigir controles ausentes ou diferenças sem justificativa e repetir as verificações afetadas. Não declarar conclusão sem essa comparação.

## Relatar evidências

Informar comandos executados e resultados; rotas e viewports cobertos; caminhos das screenshots abertas; inventário reconciliado, incluindo comportamentos pendentes e justificativa de cada diferença; achados resolvidos; justificativas de tracking, bordas e descrições; requisitos não aplicáveis com motivo; impedimentos e pendências. Um scanner sem achados ou uma compilação bem-sucedida não substitui essa auditoria.
