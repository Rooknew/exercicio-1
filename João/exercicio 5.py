nome = input("Digite seu nome: ")
genero = input("Digite seu gênero (masculino/feminino/outro): ")
altura = float(input("Digite a sua altura em metros: "))

if altura >= 1.74:
    print(f"Olá, {nome}! Você é uma pessoa {genero} alta.")
else:
    print(f"Olá, {nome}! Você é uma pessoa {genero} pequena.")



