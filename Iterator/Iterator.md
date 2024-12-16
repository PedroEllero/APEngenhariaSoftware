Intenção:

O Iterator é um padrão de design comportamental que permite percorrer elementos de uma coleção sem expor sua representação subjacente (lista, pilha, árvore etc.).

Problema:

As coleções são um dos tipos de dados mais usados em programação. No entanto, uma coleção é apenas um contêiner para um grupo de objetos.

A maioria das coleções armazena seus elementos em listas simples. Entretanto, algumas delas são baseadas em pilhas, árvores, grafos e outras estruturas de dados complexas.

Mas, independentemente de como uma coleção é estruturada, ela deve fornecer alguma forma de acessar seus elementos para que outro código possa usá-los. Deve haver uma maneira de percorrer cada elemento da coleção sem acessar os mesmos elementos repetidamente.

Isso pode parecer uma tarefa fácil se você tiver uma coleção baseada em uma lista. Basta fazer um loop sobre todos os elementos. Mas como percorrer sequencialmente os elementos de uma estrutura de dados complexa, como uma árvore? Por exemplo, em um dia você pode se dar bem com a passagem em profundidade de uma árvore. No dia seguinte, porém, você pode precisar da passagem em profundidade. E, na semana seguinte, talvez você precise de outra coisa, como acesso aleatório aos elementos da árvore.

Acrescentar cada vez mais algoritmos transversais à coleção gradualmente obscurece sua responsabilidade principal, que é o armazenamento eficiente de dados. Além disso, alguns algoritmos podem ser adaptados para um aplicativo específico, portanto, incluí-los em uma classe de coleção genérica seria estranho.

Por outro lado, o código do cliente que deve trabalhar com várias coleções pode nem se importar com a forma como elas armazenam seus elementos. Entretanto, como todas as coleções oferecem maneiras diferentes de acessar seus elementos, você não tem outra opção a não ser acoplar seu código às classes de coleção específicas.

Solução:

A ideia principal do padrão Iterator é extrair o comportamento de travessia de uma coleção em um objeto separado chamado iterator.

Além de implementar o algoritmo em si, um objeto iterator encapsula todos os detalhes da passagem, como a posição atual e quantos elementos restam até o final. Por esse motivo, vários iterators podem percorrer a mesma coleção ao mesmo tempo, independentemente uns dos outros.

Normalmente, os iterators fornecem um método principal para buscar elementos da coleção. O cliente pode continuar executando esse método até que ele não retorne nada, o que significa que o iterator percorreu todos os elementos.

Todos os iterators devem implementar a mesma interface. Isso torna o código do cliente compatível com qualquer tipo de coleção ou qualquer algoritmo de passagem, desde que haja um iterator adequado. Se você precisar de uma maneira especial de percorrer uma coleção, basta criar uma nova classe de iterator, sem precisar alterar a coleção ou o cliente.

Analogia com o mundo real:

Você planeja visitar Roma por alguns dias e conhecer todos os seus principais pontos turísticos e atrações. Mas, uma vez lá, você pode perder muito tempo andando em círculos, sem conseguir encontrar nem mesmo o Coliseu.

Por outro lado, você pode comprar um aplicativo de guia virtual para seu smartphone e usá-lo para navegação. É inteligente e barato, e você pode ficar em alguns lugares interessantes pelo tempo que quiser.

Uma terceira alternativa é gastar parte do orçamento da viagem e contratar um guia local que conheça a cidade como a palma da mão. O guia poderá adaptar o passeio aos seus gostos, mostrar todas as atrações e contar muitas histórias interessantes. Isso será ainda mais divertido, mas, infelizmente, também mais caro.

Todas essas opções - as direções aleatórias que nascem em sua cabeça, o navegador do smartphone ou o guia humano - atuam como iterators sobre a vasta coleção de pontos turísticos e atrações localizadas em Roma.

Pseudocódigo:

Neste exemplo, o padrão Iterator é usado para percorrer um tipo especial de coleção que encapsula o acesso ao grafo social do Facebook. A coleção fornece vários iterators que podem percorrer perfis de várias maneiras.

O iterator “friends” pode ser usado para examinar os amigos de um determinado perfil. O iterator “colleagues” faz o mesmo, mas omite os amigos que não trabalham na mesma empresa que a pessoa-alvo. Ambos os iterators implementam uma interface comum que permite que os clientes busquem perfis sem se aprofundar nos detalhes de implementação, como autenticação e envio de solicitações REST.

O código do cliente não está acoplado a classes concretas porque trabalha com coleções e iterators somente por meio de interfaces. Se você decidir conectar seu aplicativo a uma nova rede social, basta fornecer novas classes de coleção e iterator sem alterar o código existente.

Aplicabilidade:

Use o padrão Iterator quando sua coleção tiver uma estrutura de dados complexa, mas você quiser ocultar essa complexidade dos clientes (por conveniência ou por motivos de segurança):

O iterator encapsula os detalhes do trabalho com uma estrutura de dados complexa, fornecendo ao cliente vários métodos simples de acesso aos elementos da coleção. Embora essa abordagem seja muito conveniente para o cliente, ela também protege a coleção de ações descuidadas ou mal-intencionadas que o cliente poderia executar se trabalhasse diretamente com a coleção.


Use o padrão iterator para reduzir a duplicação do código transversal em seu aplicativo:

O código de algoritmos de iteração não triviais tende a ser muito volumoso. Quando colocado na lógica comercial de um aplicativo, ele pode obscurecer a responsabilidade do código original e torná-lo menos sustentável. Mover o código transversal para iterators designados pode ajudá-lo a tornar o código do aplicativo mais enxuto e limpo.


Use o iterator quando quiser que seu código seja capaz de percorrer diferentes estruturas de dados ou quando os tipos dessas estruturas forem desconhecidos de antemão:

O padrão fornece algumas interfaces genéricas para coleções e iteradores. Como seu código agora usa essas interfaces, ele ainda funcionará se você passar a ele vários tipos de coleções e iterators que implementam essas interfaces.

Como implementar:

1: Declare a interface do iterator. No mínimo, ela deve ter um método para buscar o próximo elemento de uma coleção. Mas, por conveniência, você pode adicionar alguns outros métodos, como buscar o elemento anterior, rastrear a posição atual e verificar o fim da iteração.

2: Declare a interface da coleção e descreva um método para buscar iterators. O tipo de retorno deve ser igual ao da interface do iterator. Você pode declarar métodos semelhantes se planejar ter vários grupos distintos de iterators.

3: Implemente classes de iterator concretas para as coleções que você deseja que sejam percorríveis com iterators. Um objeto iterator deve ser vinculado a uma única instância de coleção. Normalmente, esse vínculo é estabelecido por meio do construtor do iterator.

4: Implemente a interface de coleção em suas classes de coleção. A ideia principal é fornecer ao cliente um atalho para a criação de iterators, adaptados a uma classe de coleção específica. O objeto de coleção deve se passar para o construtor do iterator para estabelecer um vínculo entre eles.

5: Analise o código do cliente para substituir todo o código de passagem de coleção pelo uso de iterators. O cliente busca um novo objeto iterator toda vez que precisa iterar sobre os elementos da coleção.

Pros:

Princípio da responsabilidade única. Você pode limpar o código do cliente e as coleções extraindo algoritmos de passagem volumosos para classes separadas.

Princípio aberto/fechado. Você pode implementar novos tipos de coleções e iterators e passá-los para o código existente sem quebrar nada.

É possível iterar sobre a mesma coleção em paralelo porque cada objeto iterator contém seu próprio estado de iteração.

Pelo mesmo motivo, você pode atrasar uma iteração e continuá-la quando necessário.

Cons:

A aplicação do padrão pode ser um exagero se o seu aplicativo trabalhar apenas com coleções simples.

Usar um iterator pode ser menos eficiente do que percorrer diretamente os elementos de algumas coleções especializadas.

Relações com outros padrões:

Você pode usar iterators para percorrer árvores Composite.

Você pode usar o Factory Method junto com o Iterator para permitir que as subclasses de coleções retornem diferentes tipos de iterators compatíveis com as coleções.

Você pode usar o Memento junto com o Iterator para capturar o estado atual da iteração e revertê-lo, se necessário.

Você pode usar Visitor junto com Iterator para percorrer uma estrutura de dados complexa e executar alguma operação em seus elementos, mesmo que todos tenham classes diferentes.



[Exemplo de código em python](https://github.com/PedroEllero/APEngenhariaSoftware/blob/main/Iterator/Exemplo.py)

