Intenção:

O Composite é um padrão de design estrutural que permite compor objetos em estruturas de árvore e, em seguida, trabalhar com essas estruturas como se fossem objetos individuais.

Problema:

O uso do padrão Composite só faz sentido quando o modelo principal do seu aplicativo pode ser representado como uma árvore.

Por exemplo, imagine que você tenha dois tipos de objetos: Products e Boxes. Uma Box pode conter vários produtos, bem como várias Boxes menores. Essas pequenas Boxes também podem conter alguns Products ou Boxes ainda menores, e assim por diante.

Digamos que você decida criar um sistema de pedidos que use essas classes. Os pedidos podem conter produtos simples sem embalagem, bem como caixas cheias de produtos... e outras caixas. Como você determinaria o preço total de um pedido desse tipo?

Você poderia tentar a abordagem direta: desembrulhar todas as caixas, examinar todos os produtos e calcular o total. Isso seria possível no mundo real, mas, em um programa, não é tão simples quanto executar um loop. Você precisa conhecer as classes de Products e Boxes que está percorrendo, o nível de aninhamento das Boxes e outros detalhes desagradáveis de antemão. Tudo isso torna a abordagem direta muito incômoda ou até mesmo impossível.

Solução:
O padrão Composite sugere que você trabalhe com Products e Boxes por meio de uma interface comum que declare um método para calcular o preço total.

Como esse método funcionaria? Para um Product, ele simplesmente retornaria o preço do Product. Para uma Box, ele examinaria cada item que a Box contém, perguntaria seu preço e, em seguida, retornaria um total para essa Box. Se um desses itens fosse uma box menor, essa box também começaria a analisar seu conteúdo e assim por diante, até que os preços de todos os componentes internos fossem calculados. Uma box poderia até mesmo adicionar algum custo extra ao preço final, como o custo da embalagem.

A maior vantagem dessa abordagem é que você não precisa se preocupar com as classes concretas de objetos que compõem a árvore. Não é necessário saber se um objeto é um produto simples ou uma caixa sofisticada. Você pode tratar todos eles da mesma forma por meio da interface comum. Quando você chama um método, os próprios objetos passam a solicitação pela árvore.

Analogia com o mundo real:

Os exércitos da maioria dos países são estruturados como hierarquias. Um exército é composto por várias divisões; uma divisão é um conjunto de brigadas, e uma brigada é composta por pelotões, que podem ser divididos em esquadrões. Por fim, um esquadrão é um pequeno grupo de soldados reais. As ordens são dadas no topo da hierarquia e passadas para cada nível até que cada soldado saiba o que precisa ser feito.

Pseudocódigo:

Neste exemplo, o padrão Composite permite que você implemente o empilhamento de formas geométricas em um editor gráfico.

A classe CompoundGraphic é um contêiner que pode conter qualquer número de subformas, inclusive outras formas compostas. Uma forma composta tem os mesmos métodos que uma forma simples. Entretanto, em vez de fazer algo por conta própria, uma forma composta passa a solicitação recursivamente para todos os seus filhos e “soma” o resultado.

O código do cliente trabalha com todas as formas por meio de uma única interface comum a todas as classes de forma. Assim, o cliente não sabe se está trabalhando com uma forma simples ou composta. O cliente pode trabalhar com estruturas de objetos muito complexas sem ser acoplado a classes concretas que formam essa estrutura.

Aplicabilidade:

Use o padrão Composite quando precisar implementar uma estrutura de objetos em forma de árvore:

O padrão Composite oferece dois tipos básicos de elementos que compartilham uma interface comum: folhas simples e contêineres complexos. Um contêiner pode ser composto tanto de folhas quanto de outros contêineres. Isso permite que você construa uma estrutura de objeto recursiva aninhada que se assemelha a uma árvore.


Use o padrão quando quiser que o código do cliente trate os elementos simples e complexos de maneira uniforme:

Todos os elementos definidos pelo padrão Composite compartilham uma interface comum. Usando essa interface, o cliente não precisa se preocupar com a classe concreta dos objetos com os quais trabalha.

Como implementar:

1: Certifique-se de que o modelo principal do seu aplicativo possa ser representado como uma estrutura em árvore. Tente dividi-lo em elementos simples e contêineres. Lembre-se de que os contêineres devem ser capazes de conter tanto elementos simples quanto outros contêineres.

2: Declare a interface do componente com uma lista de métodos que façam sentido para componentes simples e complexos.

3: Crie uma classe folha para representar elementos simples. Um programa pode ter várias classes folhas diferentes.

4: Crie uma classe de contêiner para representar elementos complexos. Nessa classe, forneça um campo de matriz para armazenar referências a subelementos. A matriz deve ser capaz de armazenar folhas e contêineres, portanto, certifique-se de que ela seja declarada com o tipo de interface de componente.

Ao implementar os métodos da interface do componente, lembre-se de que um contêiner deve delegar a maior parte do trabalho aos subelementos.

5: Por fim, defina os métodos para adicionar e remover elementos filhos no contêiner.

Lembre-se de que essas operações podem ser declaradas na interface do componente. Isso violaria o Princípio de Segregação de Interface porque os métodos estarão vazios na classe folha. No entanto, o cliente poderá tratar todos os elementos da mesma forma, mesmo quando estiver compondo a árvore.

Pros:

Você pode trabalhar com estruturas de árvore complexas de forma mais conveniente: use o polimorfismo e a recursão a seu favor.

Princípio aberto/fechado. Você pode introduzir novos tipos de elementos no aplicativo sem quebrar o código existente, que agora funciona com a árvore de objetos.

Cons:

Pode ser difícil fornecer uma interface comum para classes cuja funcionalidade seja muito diferente. Em determinados cenários, você precisaria generalizar demais a interface do componente, tornando-a mais difícil de compreender.

Relações com outros padrões:

Você pode usar o Builder ao criar árvores Composite complexas porque pode programar suas etapas de construção para trabalhar recursivamente.

O Chain of Responsibility é frequentemente usado em conjunto com o Composite. Nesse caso, quando um componente folha recebe uma solicitação, ele pode passá-la pela cadeia de todos os componentes pai até a raiz da árvore de objetos.

You can use Iterators to traverse Composite trees.

You can use Visitor to execute an operation over an entire Composite tree.

You can implement shared leaf nodes of the Composite tree as Flyweights to save some RAM.

O Composite e o Decorator têm diagramas de estrutura semelhantes, pois ambos dependem da composição recursiva para organizar um número ilimitado de objetos.

Um Decorator é como um Composite, mas tem apenas um componente filho. Há outra diferença significativa: O Decorator acrescenta responsabilidades adicionais ao objeto envolvido, enquanto o Composite apenas “soma” os resultados de seus filhos.

No entanto, os padrões também podem cooperar: você pode usar o Decorator para estender o comportamento de um objeto específico na árvore Composite.

Os designs que fazem uso intenso do Composite e do Decorator geralmente podem se beneficiar do uso do Prototype. A aplicação do padrão permite que você clone estruturas complexas em vez de reconstruí-las do zero.






