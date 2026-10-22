
class Animal:
    def __init__(self, nome, cor, peso):
        self.nome = nome
        self.cor = cor
        self.peso = peso

    def andar(self):
        print(f"{self.nome} está andando.")

    def correr(self):
        print(f"{self.nome} está correndo.")


class Cao(Animal):
    def latir(self):
        print(f"{self.nome} está latindo: Au Au!")


class Gato(Animal):
    def miar(self):
        print(f"{self.nome} está miando: Miau!")

tipo = input("Digite o tipo de animal (cao/gato): ").strip().lower()
nome = input("Nome: ")
cor = input("Cor: ")
peso = float(input("Peso (kg): "))

if tipo == "cao":
    animal = Cao(nome, cor, peso)
elif tipo == "gato":
    animal = Gato(nome, cor, peso)
else:
    print("Tipo inválido!")
    exit()

animal.andar()
animal.correr()

if isinstance(animal, Cao):
    animal.latir()
elif isinstance(animal, Gato):
    animal.miar()
