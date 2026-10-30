NOME_FICHEIRO = "Kon.txt"


def ler_ficheiro(nome_ficheiro):
    """Lê o ficheiro e apresenta as frutas ordenadas, sem duplicados."""
    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as ficheiro:
            frutas = sorted({
                linha.strip()
                for linha in ficheiro
                if linha.strip()
            }, key=str.lower)

        print("\n--- FRUTAS NO FICHEIRO ---")
        if frutas:
            for fruta in frutas:
                print(f"- {fruta}")
        else:
            print("O ficheiro não contém frutas.")

        print(f"Total de frutas: {len(frutas)}")
        return frutas

    except FileNotFoundError:
        print(f"O ficheiro '{nome_ficheiro}' não existe.")
        return None
    except OSError as erro:
        print(f"Erro ao ler o ficheiro: {erro}")
        return None


def acrescentar_ficheiro(nome_ficheiro):
    """Acrescenta uma fruta sem criar duplicados."""
    fruta = input("Digite a fruta a acrescentar: ").strip()

    if not fruta:
        print("Nenhuma fruta foi introduzida.")
        return

    frutas = ler_ficheiro(nome_ficheiro)

    if frutas is None:
        frutas = []

    if any(fruta.casefold() == existente.casefold()
           for existente in frutas):
        print(f"A fruta '{fruta}' já existe no ficheiro.")
        return

    frutas.append(fruta)
    frutas.sort(key=str.lower)

    try:
        with open(nome_ficheiro, "w", encoding="utf-8") as ficheiro:
            for item in frutas:
                ficheiro.write(item + "\n")

        print(f"Fruta '{fruta}' acrescentada com sucesso!")

    except OSError as erro:
        print(f"Erro ao guardar a fruta: {erro}")


def criar_sobrescrever_ficheiro(nome_ficheiro):
    """Cria ou substitui o ficheiro com frutas ordenadas e sem duplicados."""
    frutas = {}

    print("\nIntroduza as frutas (linha vazia para terminar):")

    while True:
        fruta = input("> ").strip()

        if not fruta:
            break

        chave = fruta.casefold()
        if chave not in frutas:
            frutas[chave] = fruta

    frutas_ordenadas = sorted(frutas.values(), key=str.lower)

    try:
        with open(nome_ficheiro, "w", encoding="utf-8") as ficheiro:
            for fruta in frutas_ordenadas:
                ficheiro.write(fruta + "\n")

        print(
            f"Ficheiro '{nome_ficheiro}' guardado com "
            f"{len(frutas_ordenadas)} frutas."
        )

    except OSError as erro:
        print(f"Erro ao criar o ficheiro: {erro}")


def main():
    print("=" * 30)
    print("       PROGRAMA FRUTAS")
    print("=" * 30)
    print(f"Ficheiro selecionado: {NOME_FICHEIRO}")

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Ler as frutas")
        print("2 - Acrescentar uma fruta")
        print("3 - Criar/Sobrescrever o ficheiro")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            ler_ficheiro(NOME_FICHEIRO)

        elif opcao == "2":
            acrescentar_ficheiro(NOME_FICHEIRO)

        elif opcao == "3":
            confirmar = input(
                "Atenção: esta opção substitui o conteúdo atual. "
                "Continuar? (s/n): "
            ).strip().lower()

            if confirmar == "s":
                criar_sobrescrever_ficheiro(NOME_FICHEIRO)
            else:
                print("Operação cancelada.")

        elif opcao == "0":
            print("Programa terminado. Até à próxima!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()