# exemplo conceitual Composite em python

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    
    #   A classe Component base declara operações comuns para objetos simples e complexos de uma composição.

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
    
        #   Opcionalmente, o Component base pode declarar uma interface para definir e acessar um pai do componente
        #   em uma estrutura de árvore. Ele também pode fornecer alguma implementação padrão para esses métodos.

        

        self._parent = parent

    
    #   Em alguns casos, seria vantajoso definir as operações de gerenciamento de filhos diretamente na classe base do Component.
    #   Dessa forma, você não precisará expor nenhuma classe de componente concreto ao código do cliente,
    #   nem mesmo durante a montagem da árvore de objetos.
    #   A desvantagem é que esses métodos ficarão vazios para os componentes de nível de folha.

    

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        
        # Você pode fornecer um método que permita que o código do cliente descubra se um componente pode ter filhos.


        return False

    @abstractmethod
    def operation(self) -> str:
        
        #   O Component de base pode implementar algum comportamento padrão ou deixá-lo para as classes concretas
        #   (declarando o método que contém o comportamento como “abstrato”).


        pass


class Leaf(Component):
   
    #   A classe Leaf representa os objetos finais de uma composição. Uma folha não pode ter filhos.

    #   Normalmente, são os objetos Leaf que fazem o trabalho real, 
    #   enquanto os objetos Composite apenas delegam aos seus subcomponentes.

    

    def operation(self) -> str:
        return "Folha"


class Composite(Component):

    #   A classe Composite representa os componentes complexos que podem ter filhos.
    #   Normalmente, os objetos Composite delegam o trabalho real aos seus filhos e, em seguida, “somam” o resultado.


    def __init__(self) -> None:
        self._children: List[Component] = []

    
    #   Um objeto Composite pode adicionar ou remover outros componentes (simples ou complexos) de ou para sua lista de filhos.

    

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        
        #   O Composite executa sua lógica primária de uma maneira específica.
        #   Ele percorre recursivamente todos os seus filhos, coletando e somando seus resultados.
        #   Como os filhos do Composite passam essas chamadas para seus filhos e assim por diante,
        #   a árvore de objetos inteira é percorrida como resultado.

    

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Ramo({'+'.join(results)})"


def client_code(component: Component) -> None:
    
    #   O código do cliente funciona com todos os componentes por meio da interface básica.

    print(f"RESULTADO: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    
    #   Graças ao fato de as operações de gerenciamento de filhos serem declaradas na classe Component de base,
    #   O código do cliente pode trabalhar com qualquer componente, simples ou complexo, sem depender de suas classes concretas.


    if component1.is_composite():
        component1.add(component2)

    print(f"RESULTADO: {component1.operation()}", end="")


if __name__ == "__main__":
    #   Dessa forma, o código do cliente pode suportar os componentes simples de folha...
    simple = Leaf()
    print("Cliente: Eu tenho um componente:")
    client_code(simple)
    print("\n")

    #   ...bem como os composites complexos.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Cliente: Agora tenho uma arvore Composite:")
    client_code(tree)
    print("\n")

    print("Cliente: Nao preciso verificar as classes de componentes nem mesmo ao gerenciar a arvore:")
    client_code2(tree, simple)
