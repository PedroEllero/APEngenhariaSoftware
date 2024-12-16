Intenção:
O Builder é um padrão de design de criação que permite construir objetos complexos passo a passo. O padrão permite que você produza diferentes tipos e representações de um objeto usando o mesmo código de construção.

Problema:
Imagine um objeto complexo que requer uma inicialização meticulosa, passo a passo e de muitos campos e objetos aninhados. Esse código de inicialização geralmente está enterrado em um construtor monstruoso com muitos parâmetros. Ou pior ainda: espalhado por todo o código do cliente.

Por exemplo, vamos pensar em como criar um objeto House. Para construir uma casa simples, você precisa construir quatro paredes e um piso, instalar uma porta, colocar um par de janelas e construir um telhado. Mas e se você quiser uma casa maior e mais iluminada, com um quintal e outras coisas (como um sistema de aquecimento, encanamento e fiação elétrica)?

A solução mais simples é estender a classe House básica e criar um conjunto de subclasses para cobrir todas as combinações de parâmetros. Mas, eventualmente, você acabará com um número considerável de subclasses. Qualquer novo parâmetro, como o estilo da varanda, exigirá que essa hierarquia cresça ainda mais.

Há outra abordagem que não envolve a criação de subclasses. Você pode criar um Builder gigante diretamente na classe House base com todos os parâmetros possíveis que controlam o objeto casa. Embora essa abordagem de fato elimine a necessidade de subclasses, ela cria outro problema.

Na maioria dos casos, a maior parte dos parâmetros não será usada, tornando as chamadas do construtor muito feias. Por exemplo, apenas uma fração das casas tem piscinas, portanto, os parâmetros relacionados a piscinas serão inúteis nove em cada dez vezes.

Solução:
O padrão Builder sugere que você extraia o código de construção do objeto de sua própria classe e o mova para objetos separados chamados builders

O padrão organiza a construção de objetos em um conjunto de etapas (buildWalls, buildDoor etc.). Para criar um objeto, você executa uma série dessas etapas em um objeto construtor. A parte importante é que você não precisa chamar todas as etapas. Você pode chamar apenas as etapas necessárias para produzir uma configuração específica de um objeto.

Algumas das etapas de construção podem exigir uma implementação diferente quando você precisar criar várias representações do produto. Por exemplo, as paredes de uma cabana podem ser construídas de madeira, mas as paredes do castelo devem ser construídas com pedra.

Nesse caso, você pode criar várias classes de Builder diferentes que implementam o mesmo conjunto de etapas de construção, mas de maneira diferente. Em seguida, você pode usar esses construtores no processo de construção (ou seja, um conjunto ordenado de chamadas para as etapas de construção) para produzir diferentes tipos de objetos.

Por exemplo, imagine um construtor que constrói tudo com madeira e vidro, um segundo que constrói tudo com pedra e ferro e um terceiro que usa ouro e diamantes. Ao chamar o mesmo conjunto de etapas, você obtém uma casa comum do primeiro construtor, um pequeno castelo do segundo e um palácio do terceiro. No entanto, isso só funcionaria se o código do cliente que chama as etapas de construção fosse capaz de interagir com os construtores usando uma interface comum.

Diretor:
Você pode ir além e extrair uma série de chamadas para as etapas do Builder que você usa para construir um produto em uma classe separada chamada Director. A classe Director define a ordem de execução das etapas de construção, enquanto o builder fornece a implementação dessas etapas.

Ter uma classe Director em seu programa não é estritamente necessário. Você sempre pode chamar as etapas de construção em uma ordem específica diretamente do código do cliente. Entretanto, a classe Director pode ser um bom lugar para colocar várias rotinas de construção para que você possa reutilizá-las em seu programa.

Além disso, a classe Director oculta completamente os detalhes da construção do produto do código do cliente. O cliente só precisa associar um Builder a um diretor, iniciar a construção com o diretor e obter o resultado do Builder.

Pseudocódigo:

Este exemplo do padrão Builder ilustra como você pode reutilizar o mesmo código de construção de objetos ao criar diferentes tipos de produtos, como carros, e criar os manuais correspondentes para eles.

Se o código do cliente precisar montar um modelo especial e refinado de um carro, ele poderá trabalhar diretamente com o Builder. Por outro lado, o cliente pode delegar a montagem à classe Director, que sabe como usar um Builder para construir vários dos modelos mais populares de carros.

Talvez você fique chocado, mas todo carro precisa de um manual (sério, quem o lê?). O manual descreve todos os recursos do carro, portanto, os detalhes dos manuais variam entre os diferentes modelos. É por isso que faz sentido reutilizar um processo de construção existente tanto para carros reais quanto para seus respectivos manuais. É claro que construir um manual não é o mesmo que construir um carro, e é por isso que devemos fornecer outra classe de construtor especializada na composição de manuais. Essa classe implementa os mesmos métodos de construção que sua irmã construtora de carros, mas, em vez de criar peças de carros, ela as descreve. Ao passar esses construtores para o mesmo objeto Director, podemos construir um carro ou um manual.

A parte final é buscar o objeto resultante. Um carro de metal e um manual de papel, embora relacionados, ainda são coisas muito diferentes. Não podemos colocar um método para buscar resultados no Director sem acoplar o Director às classes de produtos concretos. Portanto, obtemos o resultado da construção do construtor que realizou o trabalho.




Aplicabilidade:

Use o padrão Builder para se livrar de um “construtor telescópico”:

Digamos que você tenha um construtor com dez parâmetros opcionais. Chamar esse monstro é muito inconveniente; portanto, você sobrecarrega o construtor e cria várias versões mais curtas com menos parâmetros. Esses construtores ainda se referem ao principal, passando alguns valores padrão para quaisquer parâmetros omitidos.

O padrão Builder permite que você construa objetos passo a passo, usando apenas as etapas de que realmente precisa. Depois de implementar o padrão, você não precisa mais colocar dezenas de parâmetros em seus construtores.


Use o padrão Builder quando quiser que seu código seja capaz de criar diferentes representações de algum produto (por exemplo, casas de pedra e de madeira):

O padrão Builder pode ser aplicado quando a construção de várias representações do produto envolve etapas semelhantes que diferem apenas nos detalhes.

A interface do Builder básico define todas as etapas de construção possíveis, e os builders concretos implementam essas etapas para construir representações específicas do produto. Enquanto isso, a classe Director orienta a ordem de construção.


Use o Builder para construir árvores compostas ou outros objetos complexos:

O padrão Builder permite que você construa produtos passo a passo. Você pode adiar a execução de algumas etapas sem interromper o produto final. Você pode até chamar as etapas recursivamente, o que é útil quando você precisa construir uma árvore de objetos.

Um Builder não expõe o produto inacabado durante a execução das etapas de construção. Isso evita que o código do cliente busque um resultado incompleto.

Como Implementar:

1: Certifique-se de que você possa definir claramente as etapas comuns de construção para construir todas as representações de produtos disponíveis. Caso contrário, você não conseguirá prosseguir com a implementação do padrão.

2: Declare essas etapas na interface base do Builder.

3: Crie uma classe Builder concreta para cada uma das representações de produto e implemente suas etapas de construção.
Não se esqueça de implementar um método para buscar o resultado da construção. O motivo pelo qual esse método não pode ser declarado dentro da interface do Builder é que vários Builders podem construir produtos que não têm uma interface comum. Portanto, você não sabe qual seria o tipo de retorno desse método. No entanto, se você estiver lidando com produtos de uma única hierarquia, o método de busca poderá ser adicionado com segurança à interface de base.

4: Pense na criação de uma classe Director. Ela pode encapsular várias maneiras de construir um produto usando o mesmo objeto construtor.

5: O código do cliente cria os objetos Builder e Director. Antes do início da construção, o cliente deve passar um objeto Builder para o Director. Normalmente, o cliente faz isso apenas uma vez, por meio de parâmetros do construtor da classe Director. O Director usa o objeto Builder em todas as construções posteriores. Há uma abordagem alternativa, em que o construtor é passado para um método de construção de produto específico do Director.

O resultado da construção pode ser obtido diretamente do Director somente se todos os produtos seguirem a mesma interface. Caso contrário, o cliente deve buscar o resultado no Builder.

Pros:
Você pode construir objetos passo a passo, adiar etapas de construção ou executar etapas recursivamente.
Você pode reutilizar o mesmo código de construção ao criar várias representações de produtos.
Princípio de responsabilidade única. Você pode isolar o código de construção complexo da lógica comercial do produto.

Cons:
A complexidade geral do código aumenta, pois o padrão exige a criação de várias classes novas.

Relações com outros padrões:
Muitos projetos começam usando o Factory Method (menos complicado e mais personalizável por meio de subclasses) e evoluem para o Abstract Factory, Prototype ou Builder (mais flexível, porém mais complicado).

O Builder concentra-se na construção de objetos complexos, passo a passo. O Abstract Factory é especializado na criação de famílias de objetos relacionados. O Abstract Factory retorna o produto imediatamente, enquanto o Builder permite que você execute algumas etapas adicionais de construção antes de buscar o produto.

Você pode usar o Builder ao criar árvores Composite complexas porque pode programar suas etapas de construção para trabalhar recursivamente.

Você pode combinar o Builder com o Bridge: a classe Director desempenha o papel de abstração, enquanto os diferentes builders atuam como implementações.

Os Abstract Factories, Builders e Prototypes podem ser implementados como Singletons.






