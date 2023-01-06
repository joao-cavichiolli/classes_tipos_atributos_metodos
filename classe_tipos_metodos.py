import datetime
import random

# Os tipos de metodos de classe são:

# @classmethod
#@staticmethod
# Private Method

## Vamos aplicar os tipos de métodos

class Livro():
    #atributo de classe
    ano_atual = datetime.date.today().year
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    # Metodo de instancia ou objeto
    def imprime(self):
        print("Esse livro é %s e o Autor %s e o ano %s"%(self.titulo,self.autor,self.ano))
    
    def anopublicacao(self):
        print("Tempo de Publicação",self.ano_atual - self.ano,'anos')

    #Metodo de Classe utiliza o decorador @classmethod

    @classmethod
    def calculoanopublicacao(vclasse,nome,ano):
        calcula = vclasse.ano_atual - ano
        return (nome,"Tempo Publicação",str(calcula),'anos')

# Método oculto basta utilizar o duplo underline

    def __autor(self):
        return(self.autor)

# Metodo do tipo estatico utiliza o decorador @staticmethod
    @staticmethod
    def geraisbn():
        isbn = random.randint(0,100)
        return isbn

