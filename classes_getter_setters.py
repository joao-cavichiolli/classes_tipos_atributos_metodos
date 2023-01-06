## Utilizando os metodos decoradores @property(getter) e o @.setter
# Utilizando boas praticas de abstração de atributos utilizamos o getters
# Para sobrever um metodo sem impactar nos objetos instanciados préviamente
#utilizamos o setter.
# Para voce utilizar um recurso de setter precisa ser utilizado o getter 
# no atributo da classe.

## Podemos deixar um atributo prova como pulbico com o @property usando
# getters

class VendaProdutos():
    
    def __init__(self,produto,quantidade,valor):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor = valor
    
    # Aplicando getter no atributo produto para abstrair o metodo utilizando
    #  getters

    @property # Função decoradora para aplicar o getter
    def produto(self):
        return self.__produto

    ## Vamos fazer um getter do atributo quantidade para apos fazer um
    # setter da quantidade

    @property
    def quantidade(self):
        return self.__quantidade

# Criando setter para aplicar a funcionalidade de alterar a quantidade
    @quantidade.setter
    def quantidade(self,nova_quantidade):
        self.__quantidade = nova_quantidade
    
# Criando um metódo atraves do getter manipulando valores dos atributos
    @property
    def valor_total_compra(self):
        return self.__quantidade * self.__valor






