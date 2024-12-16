# exemplo conceitual Iterator em python

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any



    #   Para criar um iterator em Python, há duas classes abstratas do módulo `collections` interno - Iterable, Iterator.
    #   Precisamos implementar o método `__iter__()` no objeto iterado (coleção) e o método `__next__ ()` no iterator.



class AlphabeticalOrderIterator(Iterator):

    #   Os iterators concretos implementam vários algoritmos de passagem.
    #   Essas classes armazenam a posição de passagem atual em todos os momentos.
    

    
    #   O atributo `_position` armazena a posição atual da passagem.
    #   Um iterator pode ter muitos outros campos para armazenar o estado da iteração,
    #   especialmente quando deve trabalhar com um tipo específico de coleção.
    
    _position: int = None

    
    #   Esse atributo indica a direção transversal.
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        
        #   O método __next__() deve retornar o próximo item da sequência.
        #   Ao chegar ao final, e nas chamadas subsequentes, ele deve gerar StopIteration.
        
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    
    #   As coleções Concrete Collections fornecem um ou vários métodos para recuperar novas instâncias de iterator,
    #   compatíveis com a classe da coleção.
    

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []


    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> AlphabeticalOrderIterator:
        
        #   O método __iter__() retorna o próprio objeto iterator; por padrão, retornamos o iterator em ordem crescente.
        
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)


if __name__ == "__main__":
    #   O código do cliente pode ou não saber sobre as classes Concrete Iterator ou Collection,
    #   dependendo do nível de indireção que você deseja manter em seu programa.
    collection = WordsCollection()
    collection.add_item("Primeiro")
    collection.add_item("Segundo")
    collection.add_item("Terceiro")

    print("Travessia reta:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")
