# de Samuel Augusto da Silva

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade
        if self.__idade < 0:
            self.__idade = int(input('erro no registro, digite uma nova idade: '))
    
    def exibir_dados():
        print("nome do animal: ", self.nome)
        print("idade do animal: ", self.__idade)
    
    def get_idade():
        print("idade do animal: ", self.__idade)
        
    def set_idade():
        if self.__idade >= 0:
            nova_idade = int(input("digite a nova idade: "))    
            self.__idade = nova_idade
        else:
            print("erro na nova idade")

    def emitir_som():
        print("o animal está emitindo um som")

class Cachorro(Animal):
    def emitir_som():
        print("Au Au Au")
        
class Gato(Animal):
    def emitir_som():
        print("Miau Miau")
        
class Passaro(Animal):
    def emitir_som():
        print("có có")
      
cachorro = Cachorro('Rex', 3)
gato = Gato('Mimi', 2)

# exemplo da questão (e)
passaro = Passaro('Louro', -1)