## Atributos Privados 2 underlines __
# Atributos Protegido 1 underline _

# Atributos Protegidos são atributos que são acessivel a classe que foi 
# Instanciado o objeto. Porém será inacessivel para classes filhas
# classes que irao herdar atrbutos e metodos da classe pai

# Publico self.nome = nome
# Privado self.__nome = nome
# Protected self._nome = nome 

## Classe de Exemplo para Privado(Encapsulados) Publico(Abstraidos) e Protegido

import datetime

class Pessoa():
    anoatual = datetime.date.today().year
    def __init__(self,nome,sobrenome,cpf,anonascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__cpf = cpf
        self._anonascimento = anonascimento
    
    @classmethod # metodo de classe (nao tem o self)
    def idade(vanoatual,_anonascimento):
        calculaidade = vanoatual.anoatual - _anonascimento
        print(f"Idade é: {calculaidade}")





