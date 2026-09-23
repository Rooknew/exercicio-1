nome = input("Por favor digite o seu nome : ")

quantidade = len(nome.replace(" ", ""))

print("O nome do utilizador tem", quantidade, "caracteres, sem contar os espaços.")

if quantidade>=10:
   print("Numero de Caracter do Utilizador foi Aprovado")

else:
   print("Numero de Caracter do Utilizador foi Reprovado")
