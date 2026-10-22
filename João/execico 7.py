
def calcular_imc(peso: float, altura_cm: float) -> float:
    """
    Calcula o IMC usando a fórmula: peso / (altura ** 2)
    A altura é fornecida em centímetros e convertida para metros.
    Retorna o valor do IMC arredondado para 2 casas decimais.
    """
    altura_m = altura_cm / 100  
    return round(peso / (altura_m ** 2), 2)


def classificar_imc(imc: float) -> str:
    """
    Classifica o IMC de acordo com a tabela padrão.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"


def obter_valor_float(mensagem: str) -> float:
    """
    Solicita um valor float ao utilizador com validação.
    Rejeita letras ou valores não numéricos.
    """
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = float(entrada)
            if valor <= 0:
                print(" O valor deve ser positivo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números.")


def main():
    print("=== Calculadora de IMC ===")
    peso = obter_valor_float("Utilizador, insira o seu peso (kg): ")
    altura_cm = obter_valor_float("Utilizador, insira a sua altura (cm): ")

    imc = calcular_imc(peso, altura_cm)
    classificacao = classificar_imc(imc)

    print(f"\n O seu IMC é: {imc:.2f}")
    print(f" Classificação: {classificacao}")


if __name__ == "__main__":
    main()
