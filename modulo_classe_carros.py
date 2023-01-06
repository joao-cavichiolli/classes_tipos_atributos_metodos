# Todos os atributos que estiverem dentro do metodo construtor
# __init__ e tem o namespace self são atributos de instancia(objeto)

## Os atributos de classe são declarados fora do metodo construtor
# __init__ nao tem o self


class Carros():

#Atributo de classe 
    cor = "Branca"
    
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    

    def resumocarro(self):
        print(f"Esse carro é {self.marca} e o Modelo {self.modelo}")