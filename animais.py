class Animal:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
    
    def emitir_som(self):
        print("O animal emitiu um som genérico.")

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro latiu!")

class Gato(Animal):
    def emitir_som(self):
        print("O gato miou!")

c = Cachorro("Oliver", 5)
g = Gato("Bup", 6)

print(f"O cachorro se chama {c.nome} e tem {c.idade} anos.")
c.emitir_som()

print(f"O gato se chama {g.nome} e tem {g.idade} anos.")
g.emitir_som()

print(f"O cachorro se chama {c.nome} e tem {c.idade} anos.")
print(f"O gato se chama {g.nome} e tem {g.idade} anos.")