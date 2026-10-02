palavras = ["peneu","Carro","Carlos","Ze","Pedro"]
maior = ""
menor = ""

for i in range(5):
    palavra = input(f"Digite a {i+1}ª palavra: ")
    palavras.append(palavra)

    
    if i == 0:  
        maior = palavra
        menor = palavra
    else:
        if len(palavra) > len(maior):
            maior = palavra
        if len(palavra) < len(menor):
            menor = palavra

    
    print(f"Maior até agora: {maior} ({len(maior)} caracteres)")
    print(f"Menor até agora: {menor} ({len(menor)} caracteres)\n")

print("\nPalavras digitadas:", palavras)
print("Maior palavra final:", maior, "-", len(maior), "caracteres")
print("Menor palavra final:", menor, "-", len(menor), "caracteres") 


