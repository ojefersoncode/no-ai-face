# Regras obrigatórias NO AI FACE

## 1. Princípio obrigatório

Todas as regras deste documento são requisitos de aceitação.

Não transforme obrigações em recomendações. Não use expressões como “preferencialmente”, “quando possível” ou “considere” para flexibilizar estas regras.

Não substitua ferramentas, não crie exceções por conveniência técnica ou preferência estética e não permita que o agente justifique violações com seu próprio julgamento.

Preserve somente as condições expressamente previstas neste documento.

Se um requisito não puder ser cumprido, o agente deve informar o impedimento e solicitar orientação antes de prosseguir com a parte afetada. Não pode fazer uma substituição silenciosa.

## 2. Quando ativar a skill

A skill deve ser utilizada para:

- Criar sites e aplicações.
- Desenvolver interfaces a partir de referências visuais.
- Redesenhar interfaces com aparência genérica de IA.
- Aplicar uma identidade visual nova a um projeto existente.

Em projetos existentes, o agente deve identificar incompatibilidades com estas regras e executar as mudanças necessárias dentro do escopo autorizado. Se a conformidade exigir alterações fora desse escopo, deve informar o impedimento e solicitar orientação.

## 3. Referência visual obrigatória

Antes de iniciar o desenvolvimento da interface, o agente deve solicitar uma referência de design.

São referências válidas: screenshots, imagens, arquivos de design ou URLs cujo conteúdo visual possa ser inspecionado.

Se o usuário já tiver fornecido uma referência acessível, utilize-a. Não solicite novamente o mesmo material.

Sem uma referência visual acessível:

- Não iniciar a implementação visual.
- Não inventar uma referência.
- Não substituir a referência por uma descrição estética genérica.
- Solicitar o material necessário e aguardar.

Se não conseguir inspecionar a referência, informar o impedimento. Não alegar que analisou um conteúdo que não conseguiu acessar.

### Inspeção obrigatória de referências por URL

Quando a referência visual for uma URL, tentar abri-la e capturá-la com um navegador real antes de declarar que ela está inacessível. Usar Playwright para inspecionar a página em desktop e mobile, percorrer seu conteúdo, observar controles e estados acessíveis e salvar screenshots para a análise visual e o inventário.

Verificar primeiro se já existe uma instalação utilizável de Playwright e do navegador necessário. Se faltar, instalá-los no projeto com o gerenciador de pacotes já adotado e instalar o Chromium fornecido pelo Playwright. Respeitar as permissões do ambiente. Não substituir essa etapa por uma análise baseada apenas em HTML, metadados ou resultados de busca.

A instalação deve servir tanto à inspeção da referência quanto aos testes da interface implementada. Registrar os comandos usados, as URLs e viewports inspecionados e os caminhos das capturas. Abrir e examinar as screenshots antes de implementar.

Se a URL continuar inacessível após a tentativa com navegador, registrar o erro concreto, como falha de DNS, bloqueio de rede ou erro do site. Nesse caso, solicitar uma captura ou outro arquivo visual ao usuário e aguardar antes de iniciar a implementação visual. Não afirmar que a referência foi inspecionada quando a navegação ou a captura falhou.

### Inventário obrigatório da referência

Antes de implementar, inventariar todos os elementos visíveis e estados observáveis da referência, incluindo navegação, busca, botões, formulários e menus. Para cada item, registrar onde será implementado e qual comportamento terá. Registrar estados que a referência não revela como não observados; não inventar que foram inspecionados.

Não omitir um controle por falta de backend. Preservar sua presença visual e registrar explicitamente o comportamento pendente, sem inventar um serviço ou apresentar uma ação simulada como funcional.

Antes da entrega, comparar cada item e estado inventariado com a interface implementada. Registrar presença, localização e comportamento real, justificar cada diferença em relação à referência e corrigir omissões sem justificativa. O inventário reconciliado é requisito de aceitação e deve acompanhar a entrega.

## 4. Análise da referência e branding próprio

O agente deve analisar e registrar:

- Composição e hierarquia visual.
- Tipografia e pesos.
- Paleta e contraste.
- Espaçamento e densidade.
- Uso de bordas.
- Iconografia.
- Imagens e elementos gráficos.
- Comportamento responsivo, quando observável.

A partir dessa análise, criar uma identidade visual própria para o produto, usando a referência como fundamento.

Não copiar nomes, logotipos, textos ou elementos exclusivos da marca de referência. Reinterpretar sua linguagem visual para o contexto do produto.

Definir tokens consistentes de cores, tipografia, espaçamento e demais propriedades utilizadas na implementação. Não inserir características que contradigam as proibições desta skill.

## 5. Regras visuais obrigatórias

### Eyebrows

Não utilizar eyebrows: pequenos rótulos decorativos posicionados acima de títulos.

Essa proibição não se aplica a labels funcionais de formulários, controles ou navegação.

### Tracking

Não adicionar classes `tracking-*` nem ajustes de `letter-spacing`, exceto quando esse tratamento estiver presente na referência visual e seu uso tiver sido registrado na análise.

### Enumeração decorativa

Não utilizar números como “01”, “02” e “03” apenas para decorar cards, seções ou títulos.

Números necessários para dados, quantidades ou sequências funcionais não são enumeração decorativa.

### Bordas

Não adicionar bordas a cards, containers, seções, botões, inputs ou outros elementos se esse tratamento não fizer parte da referência visual.

Cada uso de borda deve ser sustentado pela análise da referência. Não adicionar bordas automaticamente por convenção de biblioteca.

### Cores

Utilizar cores sólidas para estabelecer contraste com o background.

Não substituir essa regra por gradientes, transparências ou efeitos visuais usados como mecanismo principal de contraste.

### Travessões

Não utilizar o caractere “—” em textos da interface. Reescrever os textos usando pontuação apropriada.

## 6. Títulos e descrições

Não criar headers de telas compostos por título e descrição complementar.

Em cards, não inserir descrições por padrão.

Uma descrição em card só é permitida quando necessária para compreender ou operar seu conteúdo. O agente deve registrar uma justificativa funcional concreta para essa exceção.

Cards com gráficos ou imagens autoexplicativos não devem receber descrições redundantes.

A ausência de descrição não autoriza remover informações funcionais necessárias, como unidades, legendas de gráficos, identificação de controles e mensagens de erro.

Em cards de produtos de e-commerce, utilizar descrições relevantes ao produto. Essa é uma condição expressamente autorizada.

## 7. Stack obrigatória

### Ícones: Tabler

Utilizar Tabler Icons.

Não utilizar Lucide, incluindo imports, dependências ou ícones copiados dessa biblioteca na implementação abrangida pela skill.

### Componentes: React Aria ou React Spectrum

Utilizar React Aria Components ou Adobe React Spectrum.

Referência oficial: https://react-spectrum.adobe.com/

Não utilizar shadcn/ui, incluindo componentes copiados ou gerados a partir dele.

Escolher entre React Aria e React Spectrum conforme a capacidade de cumprir a referência e todas as demais regras. Não tratar React Aria como se fosse um tema visual pronto.

### Animações e transições: GSAP

Implementar animações e transições com GSAP.

Não substituir GSAP por outra biblioteca, animações CSS, transições CSS ou Web Animations API para executar esses efeitos.

Respeitar a preferência de movimento reduzido do usuário, reduzindo ou desativando efeitos quando necessário.

### Testes: Playwright

Utilizar Playwright para testar a interface e seus fluxos importantes.

A verificação deve incluir screenshots para revisão visual e testes de interação aplicáveis ao escopo desenvolvido.

Não considerar a tarefa validada apenas porque o código compila.

### Validação: Zod

Utilizar Zod para validar formulários e dados recebidos pelo backend.

Validação no frontend não substitui validação no backend.

Se não existir backend no escopo, registrar essa condição. Não criar um backend artificial apenas para marcar o requisito como cumprido.

### Estado global: Zustand

Utilizar Zustand para o gerenciamento de estado global.

Não substituir Zustand por Context API, Redux, Jotai ou outra solução de estado global.

Estado local de um componente pode permanecer local. Não inventar estado global desnecessário para demonstrar uso da ferramenta.

## 8. Mobile first obrigatório

Desenvolver a aplicação inteira com mobile first.

Começar pelo layout de celular e expandir para tablet e desktop.

Verificar:

- Ausência de overflow horizontal involuntário.
- Legibilidade dos textos.
- Acesso a controles e ações.
- Navegação utilizável por toque.
- Reorganização adequada de grids e conteúdo.
- Funcionamento de formulários, menus e dialogs.
- Ausência de conteúdo cortado ou sobreposto.

Não considerar mobile first apenas adicionar media queries ao final de um layout desenvolvido para desktop.

## 9. Fluxo obrigatório de execução

A skill deve instruir o agente a seguir esta sequência:

1. Verificar se existe uma referência visual acessível.
2. Solicitar a referência quando estiver ausente e aguardar.
3. Se a referência for uma URL, executar a inspeção obrigatória por navegador, abrir as capturas e registrar as evidências ou o erro concreto. Inspecionar a referência e registrar a análise.
4. Inventariar todos os elementos visíveis e estados da referência, registrando o destino de implementação e o comportamento de cada item.
5. Definir a identidade visual própria e os tokens.
6. Inspecionar o projeto e identificar conflitos com a stack obrigatória.
7. Implementar primeiro a composição mobile.
8. Adaptar para telas maiores.
9. Implementar interações, validação, estado e movimento com as ferramentas obrigatórias.
10. Executar as verificações automatizadas.
11. Executar testes e capturar screenshots com Playwright.
12. Inspecionar visualmente as screenshots.
13. Comparar o inventário com a interface implementada e justificar cada diferença.
14. Corrigir violações e omissões sem justificativa e repetir as verificações afetadas.
15. Entregar o resultado e o inventário reconciliado com evidências de conformidade.

## 10. Auditoria obrigatória

Criar scripts de verificação para o que puder ser detectado automaticamente, incluindo:

- Imports e dependências de Lucide.
- Uso de shadcn/ui e componentes identificáveis dessa origem.
- Classes `tracking-*` e declarações de `letter-spacing` que exijam revisão.
- O caractere “—” em textos da interface.
- Bibliotecas alternativas usadas para animação ou estado global.
- Animações e transições CSS incompatíveis com a regra de GSAP.

Os verificadores devem distinguir violações confirmadas de ocorrências que exigem revisão contextual.

Presença de dependências não prova uso correto. Verificar também os pontos de implementação.

A auditoria visual deve conferir:

- Ausência de eyebrows e enumeração decorativa.
- Uso de bordas sustentado pela referência.
- Cores sólidas e contraste.
- Ausência de descrições proibidas ou redundantes.
- Identidade própria derivada da referência.
- Composição mobile first.
- Presença e localização de todos os elementos e estados inventariados; diferenças justificadas.

Não alegar que um script consegue confirmar sozinho critérios subjetivos de design.

## 11. Critério de conclusão

O agente só pode declarar a tarefa concluída quando todos os requisitos aplicáveis estiverem atendidos e verificados.

O relatório final deve apresentar:

- Referência utilizada.
- Identidade visual criada.
- Regras verificadas.
- Testes executados e resultados.
- Screenshots inspecionadas.
- Inventário reconciliado com a interface implementada e justificativa de cada diferença.
- Eventuais impedimentos ainda existentes.

Não inventar testes, screenshots, resultados ou conformidade.

Uma verificação que não foi executada deve ser identificada como pendente. Um impedimento não equivale a aprovação.

