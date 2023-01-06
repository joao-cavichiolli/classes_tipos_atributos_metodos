
## OS atributos de uma classe podem ser do tipo privado protect ou publico
# Os atributos publico estão acessiveis para todos os objectos (Abstração)
# Os atributos privados podem ser instanciados porem os seus valores
# não serão acessivel para os objetos.(Encapsulamento)

## OS atributos publico são escrito de forma normal (ABSTRACAO)
# EX self.nome = nome

# Os atributo do tipo privado possuem 2 underline(dunder) na construção (ENCAPSULAMENTO)
# Ex: self.__nome = nome

class Cadastrouser():
    def __init__(self,usuario,senha):
        self.usuario = usuario # Abstraido
        self.__senha = senha # Encapsulado Atributo Privado