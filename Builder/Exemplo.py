# exemplo conceitual Builder em python

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):

    #   A interface Builder especifica métodos para criar as diferentes partes dos objetos Product.


    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    #   As classes Concrete Builder seguem a interface Builder e fornecem implementações específicas das etapas de construção.
    #   Seu programa pode ter diversas variações de Builders, implementadas de forma diferente.


    def __init__(self) -> None:
        
        #   Uma nova instância do builder deve conter um objeto de produto em branco, que é usado na montagem posterior.

        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
    
        #   Os Concrete Builders devem fornecer seus próprios métodos para recuperar resultados.
        #   Isso ocorre porque vários tipos de construtores podem criar produtos totalmente diferentes que não seguem a mesma interface. Portanto, esses métodos não podem ser declarados na interface base do Builder (pelo menos em uma linguagem de programação estaticamente tipada).

        #   Normalmente, depois de devolver o resultado final ao cliente,
        #   espera-se que uma instância do construtor esteja pronta para começar a produzir outro produto.
        #   É por isso que é uma prática comum chamar o método reset no final do corpo do método “getProduct”.
        #   Entretanto, esse comportamento não é obrigatório, e você pode fazer com que
        #   seus construtores aguardem uma chamada explícita de reset do código do cliente antes de descartar o resultado anterior.

        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("ParteA1")

    def produce_part_b(self) -> None:
        self._product.add("ParteB1")

    def produce_part_c(self) -> None:
        self._product.add("ParteC1")


class Product1():
    
    #   Faz sentido usar o padrão Builder somente quando seus produtos são bastante complexos e exigem uma configuração extensa.

    #   Ao contrário de outros padrões de criação, diferentes construtores de concreto podem produzir produtos não relacionados.
    #   Em outras palavras, os resultados de vários construtores podem nem sempre seguir a mesma interface.


    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes do Produto: {', '.join(self.parts)}", end="")


class Director:
    
    #   O Director é responsável apenas pela execução das etapas de construção em uma sequência específica.
    #   Ele é útil na produção de produtos de acordo com uma ordem ou configuração específica.
    #   A rigor, a classe Director é opcional, pois o cliente pode controlar os construtores diretamente.


    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        
        #   O Director trabalha com qualquer instância do construtor que o código do cliente passa para ele.
        #   Dessa forma, o código do cliente pode alterar o tipo final do produto recém-montado.

        
        self._builder = builder

        #   O Director pode construir diversas variações de produtos usando as mesmas etapas de construção.


    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    
    #   O código do cliente cria um objeto builder, passa-o para o Director e, em seguida, inicia o processo de construção.
    #   O resultado final é recuperado do objeto builder.


    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Produto basico padrao: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Produto padrao com todos os recursos: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    #   Lembre-se de que o padrão Builder pode ser usado sem uma classe Director.
    print("Produto customizado: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()