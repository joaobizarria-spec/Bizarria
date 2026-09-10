"""
EXEMPLO DE ESTRUTURAS DE SELECAO EM PYTHON
Sistema de gerenciamento de biblioteca e menu de opcoes
COM ENTRADA DE DADOS PELO USUARIO
"""

# ============================================
# 1. ESTRUTURA ANINHADA (if dentro de if)
# ============================================

def verificar_emprestimo():
    """
    Verifica se uma pessoa pode pegar um livro emprestado.
    """

    print("\n=== VERIFICACAO DE EMPRESTIMO ===")

    idade = int(input("Digite a idade: "))
    livros_atrasados = int(input("Digite a quantidade de livros atrasados: "))

    print(f"Idade: {idade} - Livros atrasados: {livros_atrasados}")

    if idade >= 16:
        print("Idade permitida")

        if livros_atrasados == 0:
            print("RESULTADO: EMPRESTIMO LIBERADO")
        else:
            print("RESULTADO: EMPRESTIMO BLOQUEADO - Existem livros atrasados")
    else:
        print("RESULTADO: EMPRESTIMO BLOQUEADO - Idade abaixo de 16 anos")


# ============================================
# 2. ESTRUTURA ENCADEADA COM ELIF
# ============================================

def classificar_livro():
    """
    Classifica um livro de acordo com sua avaliacao.
    """

    print("\n=== CLASSIFICACAO DO LIVRO ===")

    nota = float(input("Digite a nota do livro (0 a 10): "))

    print(f"Nota: {nota}")

    if nota >= 9.0:
        classificacao = "EXCELENTE"
    elif nota >= 7.0:
        classificacao = "MUITO BOM"
    elif nota >= 5.0:
        classificacao = "REGULAR"
    elif nota >= 3.0:
        classificacao = "FRACO"
    else:
        classificacao = "RUIM"

    print(f"CLASSIFICACAO: {classificacao}")


# ============================================
# 3. ESTRUTURA MATCH CASE
# ============================================

def processar_menu():
    """
    Processa opcoes da biblioteca usando match case.
    """

    print("\n=== MENU DA BIBLIOTECA ===")
    print("1 - Consultar livros")
    print("2 - Cadastrar livro")
    print("3 - Realizar emprestimo")
    print("4 - Sair")

    opcao = input("Digite a opcao desejada: ")

    match opcao:

        case "1":
            print("OPCAO 1: Consultar livros")

        case "2":
            print("OPCAO 2: Cadastrar livro")

        case "3":
            print("OPCAO 3: Realizar emprestimo")

        case "4" | "sair":
            print("OPCAO 4: Sair da biblioteca")

        case _:
            print(f"OPCAO INVALIDA: {opcao}")


# ============================================
# 4. MATCH CASE COM GUARDA
# ============================================

def avaliar_leitor():
    """
    Avalia a situacao de um leitor usando match case com guarda.
    """

    print("\n=== AVALIACAO DO LEITOR ===")

    nome = input("Digite o nome do leitor: ")
    livros = int(input("Digite a quantidade de livros emprestados: "))
    atrasados = int(input("Digite a quantidade de livros atrasados: "))

    print(f"Leitor: {nome} - Livros: {livros} - Atrasados: {atrasados}")

    dados = (livros, atrasados)

    match dados:

        case (qtd, _) if qtd >= 10:
            print(f"{nome}: LEITOR FREQUENTE - {qtd} livros emprestados")

        case (qtd, atraso) if qtd >= 5 and atraso == 0:
            print(f"{nome}: LEITOR ATIVO - {qtd} livros emprestados")

        case (qtd, atraso) if qtd >= 1 and atraso == 0:
            print(f"{nome}: LEITOR REGULAR - {qtd} livros emprestados")

        case (qtd, atraso) if qtd == 0 or atraso > 0:
            print(f"{nome}: SITUACAO PENDENTE - Livros {qtd}, Atrasados {atraso}")

        case _:
            print(f"{nome}: SITUACAO INDEFINIDA")


# ============================================
# 5. FUNCAO PRINCIPAL COM MENU INTERATIVO
# ============================================

def main():

    print("=" * 50)
    print("SISTEMA DE BIBLIOTECA")
    print("Demonstracao de estruturas de selecao")
    print("=" * 50)

    while True:

        print("\n" + "-" * 50)
        print("MENU PRINCIPAL")
        print("-" * 50)

        print("1 - Verificar Emprestimo")
        print("2 - Classificar Livro")
        print("3 - Processar Menu")
        print("4 - Avaliar Leitor")
        print("5 - Sair")

        opcao = input("\nEscolha uma opcao (1-5): ")

        if opcao == "1":
            verificar_emprestimo()

        elif opcao == "2":
            classificar_livro()

        elif opcao == "3":
            processar_menu()

        elif opcao == "4":
            avaliar_leitor()

        elif opcao == "5":
            print("\nSaindo do sistema...")
            break

        else:
            print("\nOPCAO INVALIDA! Tente novamente.")

        input("\nPressione Enter para continuar...")


# ============================================
# 6. FUNCOES ADICIONAIS COM ENTRADA DO USUARIO
# ============================================

def verificar_multiplos_leitores():

    print("\n=== VERIFICAR MULTIPLOS LEITORES ===")

    continuar = "s"

    while continuar.lower() == "s":

        print("\n" + "-" * 30)

        verificar_emprestimo()

        continuar = input("\nVerificar outro leitor? (s/n): ")


def classificar_multiplos_livros():

    print("\n=== CLASSIFICAR MULTIPLOS LIVROS ===")

    continuar = "s"

    while continuar.lower() == "s":

        print("\n" + "-" * 30)

        classificar_livro()

        continuar = input("\nClassificar outro livro? (s/n): ")


# ============================================
# 7. EXEMPLO DE USO COM LISTAS
# ============================================

def processar_lista_leitores():

    print("\n=== PROCESSAR LISTA DE LEITORES ===")

    leitores = []
    continuar = "s"

    while continuar.lower() == "s":

        print("\n" + "-" * 30)

        nome = input("Nome do leitor: ")
        livros = int(input("Quantidade de livros: "))
        atrasados = int(input("Quantidade de atrasados: "))

        leitores.append({
            "nome": nome,
            "livros": livros,
            "atrasados": atrasados
        })

        continuar = input("Adicionar outro leitor? (s/n): ")

    if leitores:

        print("\n" + "-" * 30)
        print("RESULTADOS:")
        print("-" * 30)

        for leitor in leitores:

            dados = (leitor["livros"], leitor["atrasados"])

            match dados:

                case (qtd, _) if qtd >= 10:
                    status = f"{leitor['nome']}: LEITOR FREQUENTE - {qtd} livros"

                case (qtd, atraso) if qtd >= 5 and atraso == 0:
                    status = f"{leitor['nome']}: LEITOR ATIVO - {qtd} livros"

                case (qtd, atraso) if qtd >= 1 and atraso == 0:
                    status = f"{leitor['nome']}: LEITOR REGULAR - {qtd} livros"

                case (qtd, atraso) if qtd == 0 or atraso > 0:
                    status = f"{leitor['nome']}: SITUACAO PENDENTE - Livros {qtd}, Atrasados {atraso}"

                case _:
                    status = f"{leitor['nome']}: SITUACAO INDEFINIDA"

            print(status)


# ============================================
# 8. MENU AVANCADO COM MATCH CASE
# ============================================

def menu_avancado():

    print("=" * 50)
    print("BIBLIOTECA - MENU AVANCADO")
    print("=" * 50)

    while True:

        print("\n" + "-" * 50)
        print("OPCOES:")
        print("-" * 50)

        print("1 - Verificar Emprestimo")
        print("2 - Classificar Livro")
        print("3 - Processar Menu")
        print("4 - Avaliar Leitor")
        print("5 - Verificar Multiplos Leitores")
        print("6 - Classificar Multiplos Livros")
        print("7 - Processar Lista de Leitores")
        print("8 - Sair")

        opcao = input("\nEscolha uma opcao: ")

        match opcao:

            case "1":
                verificar_emprestimo()

            case "2":
                classificar_livro()

            case "3":
                processar_menu()

            case "4":
                avaliar_leitor()

            case "5":
                verificar_multiplos_leitores()

            case "6":
                classificar_multiplos_livros()

            case "7":
                processar_lista_leitores()

            case "8" | "sair":
                print("\nSaindo do sistema...")
                break

            case _:
                print("\nOPCAO INVALIDA! Tente novamente.")

        if opcao != "8":
            input("\nPressione Enter para continuar...")


# ============================================
# 9. FUNCAO DE TESTE RAPIDO
# ============================================

def testar_rapido():

    print("\n=== TESTE RAPIDO ===")

    print("1 - Testar Emprestimo")
    print("2 - Testar Classificacao")
    print("3 - Testar Menu")
    print("4 - Testar Leitor")

    opcao = input("Escolha um teste (1-4): ")

    if opcao == "1":
        verificar_emprestimo()

    elif opcao == "2":
        classificar_livro()

    elif opcao == "3":
        processar_menu()

    elif opcao == "4":
        avaliar_leitor()

    else:
        print("Opcao invalida!")


# ============================================
# PONTO DE ENTRADA
# ============================================

if __name__ == "__main__":

    print("=" * 50)
    print("BIBLIOTECA - VERSOES DISPONIVEIS")
    print("=" * 50)

    print("1 - Menu Interativo")
    print("2 - Menu Avancado com Match Case")
    print("3 - Teste Rapido")
    print("4 - Sair")

    versao = input("\nEscolha uma versao (1-4): ")

    if versao == "1":
        main()

    elif versao == "2":
        menu_avancado()

    elif versao == "3":
        testar_rapido()

    elif versao == "4":
        print("Saindo...")

    else:
        print("Opcao invalida!")