import random

def jogo_adivinhacao():
    print("=== Jogo: Adivinhe o Número ===")

    
    limite_inferior = random.randint(1, 10)
    limite_superior = random.randint(limite_inferior + 10, limite_inferior + 50)

    print(f"O número secreto está entre {limite_inferior} e {limite_superior}.")

   
    numero_secreto = random.randint(limite_inferior, limite_superior)

    tentativas = 0

    while True:
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print(" Entrada inválida! Digite apenas números inteiros.")
            continue

       
        if palpite < limite_inferior or palpite > limite_superior:
            print(f" O número deve estar entre {limite_inferior} e {limite_superior}.")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print(" O número secreto é maior.")
        elif palpite > numero_secreto:
            print(" O número secreto é menor.")
        else:
            print(f" Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogo_adivinhacao()

