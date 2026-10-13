# Exemplos de decisões

| Situação | Comportamento correto | Comportamento incorreto |
|---|---|---|
| Pedido de dashboard sem referência | Solicitar imagem, arquivo ou URL visual acessível e aguardar antes da implementação | Inventar um dashboard minimalista como referência |
| Screenshot já fornecida | Inspecionar e registrar sua linguagem visual | Pedir novamente a mesma referência |
| URL inacessível | Informar que não conseguiu inspecionar e pedir material acessível | Alegar que analisou o site pelo título |
| Projeto com Lucide e shadcn | Substituir no escopo por Tabler e Aria/Spectrum; pedir orientação se ultrapassar escopo | Manter por conveniência ou copiar os mesmos SVGs |
| Hover animado por CSS | Executar transição com GSAP e respeitar movimento reduzido | Usar transition-all por ser simples |
| Estado global existente em Redux | Migrar a parte autorizada para Zustand; expor impedimentos fora do escopo | Substituir por Context API |
| Apenas estado de abertura de um componente | Manter estado local | Inventar store global para marcar requisito |
| Referência com borda em inputs | Registrar evidência e aplicar o tratamento pertinente | Acrescentar borda a todos os cards |
| Tracking visível em um título de referência | Registrar tratamento observado e aplicação específica | Aplicar tracking-wide sem justificativa |
| Card com gráfico autoexplicativo | Manter título, unidades e legenda; remover descrição redundante | Adicionar texto dizendo que o gráfico mostra dados |
| Card cujo controle exige explicação | Manter explicação necessária e registrar motivo concreto | Remover orientação que impede operação correta |
| Card de produto de e-commerce | Incluir descrição relevante do produto | Remover toda descrição por regra genérica |
| Backend existente | Validar suas entradas com Zod além da validação cliente | Validar somente no navegador |
| Playwright não executou | Relatar impedimento e validação pendente | Declarar tudo validado porque compilou |
