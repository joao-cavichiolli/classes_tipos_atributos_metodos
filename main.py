## Contexto Principal de execução do Projeto

from modulo_classe_carros import Carros 

from classe_atributos_publico_privados import Cadastrouser

from classes_abstracao_encapsulamento import Pessoa

from classes_getter_setters import VendaProdutos

from classe_tipos_metodos import Livro

## Instanciar os objetos da classe carros

carro1 = Carros("Corsa","Chevrolet")
carro2 = Carros("Ranger","Ford")

# Mostrar o valor dos objetos

print(carro1.marca)
print(carro2.modelo)

carro1.resumocarro()
carro2.resumocarro()

# Trazer o atributo de classe

print(carro1.cor)
print(carro2.cor)

## Jeito correto de exibir o atributo de classe e exibindo a classe
# e não o objeto

print(Carros.cor)


# Detalhando os valores da classe com metodo __dict__
print(Carros.__dict__)

# Detalhando os valores de uma instancia(objeto) com metodo __dict__
print(carro1.__dict__)

# Instanciar objetos da classe CadastroUsers

user1 = Cadastrouser('joao',123456)

## Consultar os valores da instancia

print(user1.usuario)
#print(user1.__senha)

## Acessando os valor de um atributos privado com a função dir
#A funcao retorna todas as propriedades e metodos de um objeto

print(dir(user1))

# Exibir atributos ocultos atraves de Naming Mangling

print(user1._Cadastrouser__senha)

## Apagando o atributo de um usuario

del user1.usuario

print(user1.__dict__)


## Criando instancias da Classe Pessoa

p1 = Pessoa("João","Cavichiolli",44444,1985)

## Exibir Atributos Publico

print(p1.nome)

## Exibir um atributo do tipo Protected(Protegido)

print(p1._anonascimento)

# Exibindo o metodo da classe 

p1.idade(1985)

## Exibir atributos privados

#print(p1.__cpf)

#Exibindo atributos Privado com NAming Mangling

print(p1._Pessoa__cpf)

#######################################################################

# Instanciando Objetos da classe VendaProdutos

produto1 = VendaProdutos("Arroz",23,10.56)

# Tentando acessar um atributo privado
#print(produto1.__produto)

# Exibindo o valor da instancia atraves do metodo getter

print(produto1.produto)


# Mostrando a quantidade atraves do Getter pois deixou acessivel
print(produto1.quantidade)

# Utilizando o setter para mudar o valor de quantidade em tempo de execução
# Sem recriar o objeto

produto1.quantidade = 50

print(f"Nova Quantidade {produto1.quantidade}")

print(produto1.valor_total_compra)


produto2 = VendaProdutos("Feijão",10,20.41)

print(produto2.valor_total_compra)

###########################################################################

# Trabalhando com Métodos de Classe

livro1 = Livro("O Pescador","José Cunha",1998)
livro1.imprime()
livro1.anopublicacao()

## Executando métodos de classe
livro3 = Livro.calculoanopublicacao("Receita de Feijoada",2009)

print(livro3)

# Chamando o metodo oculto
print(livro1._Livro__autor()) # Aplique naming Mangling

print(livro1.geraisbn())

print(livro1.__dict__)




