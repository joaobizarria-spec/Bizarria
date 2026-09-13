"""
ATIVIDADE 6 - SISTEMA DE CONTROLE DE ESTOQUE

Proposta:
Demonstra diferentes tipos de laços de repetição em Python
por meio de um pequeno sistema de controle de estoque.

Conceitos utilizados:
- while com contadora
- while com acumuladora
- while com flag
- while + if
- break e continue
- for com range
- for com listas
- laços aninhados
- validação de entrada
- menu interativo
"""

# ============================================
# FUNÇÕES AUXILIARES
# ============================================

def validar_quantidade(mensagem):
    """
    Valida uma quantidade inteira maior ou igual a zero.
    """

    while True:
        try:
            quantidade = int(input(mensagem))

            if quantidade >= 0:
                return quantidade

            print("ERRO: A quantidade não pode ser negativa.")

        except ValueError:
            print("ERRO: Digite um número inteiro válido.")


def validar_opcao(mensagem, opcoes_validas):
    """
    Valida uma opção de menu.
    """

    while True:
        opcao = input(mensagem).strip()

        if opcao in opcoes_validas:
            return opcao

        print(
            f"ERRO: Opção inválida. "
            f"Opções: {', '.join(opcoes_validas)}"
        )


# ============================================
# 1. WHILE COM CONTADORA
# ============================================

def exemplo_contadora():
    """
    Conta caixas numeradas de 1 a 5.
    """

    print("\n=== EXEMPLO 1: CONTADORA ===")
    print("Conferindo caixas do estoque:")

    caixa = 1

    while caixa <= 5:
        print(f"  Caixa {caixa} conferida.")
        caixa += 1

    print(f"Total de caixas conferidas: {caixa - 1}")


# ============================================
# 2. WHILE COM ACUMULADORA
# ============================================

def exemplo_acumuladora():
    """
    Soma as quantidades de produtos de cinco caixas.
    """

    print("\n=== EXEMPLO 2: ACUMULADORA ===")

    total = 0
    caixa = 1

    while caixa <= 5:
        quantidade = validar_quantidade(
            f"Quantidade da caixa {caixa}: "
        )

        total += quantidade
        caixa += 1

    print(f"\nTotal de produtos armazenados: {total}")


# ============================================
# 3. WHILE COM FLAG
# ============================================

def exemplo_flag():
    """
    Mantém o sistema de consulta ativo até o usuário sair.
    """

    print("\n=== EXEMPLO 3: WHILE COM FLAG ===")
    print("Digite 'sair' para encerrar a consulta.")

    sistema_ativo = True
    consultas = 0

    while sistema_ativo:
        comando = input(
            "Digite 'estoque', 'ajuda' ou 'sair': "
        ).strip().lower()

        consultas += 1

        if comando == "sair":
            sistema_ativo = False
            print(
                f"Sistema encerrado após "
                f"{consultas} comandos."
            )

        elif comando == "ajuda":
            print("Comandos disponíveis: estoque, ajuda, sair")

        elif comando == "estoque":
            print("Estoque atual: 42 unidades cadastradas.")

        else:
            print("Comando não reconhecido.")


# ============================================
# 4. WHILE + IF
# ============================================

def exemplo_nivel_estoque():
    """
    Classifica produtos como suficientes ou em reposição.
    """

    print("\n=== EXEMPLO 4: WHILE + IF ===")

    produto = 1

    while produto <= 6:
        quantidade = validar_quantidade(
            f"Quantidade do produto {produto}: "
        )

        if quantidade >= 20:
            print("  Situação: ESTOQUE NORMAL")
        else:
            print("  Situação: NECESSITA REPOSIÇÃO")

        produto += 1


# ============================================
# 5. BREAK E CONTINUE
# ============================================

def exemplo_break_continue():
    """
    Demonstra break e continue em situações de estoque.
    """

    print("\n=== EXEMPLO 5: BREAK E CONTINUE ===")

    print("Exemplo 1: BREAK - procurando um produto")
    print("Digite 'encontrado' para finalizar ou 'cancelar' para sair.")

    while True:
        comando = input("  Digite o resultado da busca: ").strip().lower()

        if comando == "cancelar":
            print("  Busca cancelada.")
            break

        if comando == "encontrado":
            print("  Produto localizado!")
            break

        print("  Produto ainda não localizado.")

    print("\nExemplo 2: CONTINUE - ignorando produtos sem estoque")

    quantidades = [8, 0, 15, 0, 23, 4]

    for quantidade in quantidades:
        if quantidade == 0:
            continue

        print(f"  Produto disponível: {quantidade} unidades")


# ============================================
# 6. FOR COM RANGE
# ============================================

def exemplo_for_range():
    """
    Demonstra diferentes formas de usar range().
    """

    print("\n=== EXEMPLO 6: FOR COM RANGE() ===")

    print("1. Prateleiras de 1 a 5:")
    for prateleira in range(1, 6):
        print(f"  Prateleira {prateleira}", end=" ")
    print()

    print("\n2. Códigos de 10 a 14:")
    for codigo in range(10, 15):
        print(f"  Código {codigo}", end=" ")
    print()

    print("\n3. Números pares de 2 a 10:")
    for numero in range(2, 11, 2):
        print(f"  {numero}", end=" ")
    print()


# ============================================
# 7. FOR COM LISTAS
# ============================================

def exemplo_for_listas():
    """
    Percorre uma lista de produtos.
    """

    print("\n=== EXEMPLO 7: FOR COM LISTAS ===")

    produtos = [
        "Teclado",
        "Mouse",
        "Monitor",
        "Fone",
        "Webcam"
    ]

    print("Produtos cadastrados:")

    for produto in produtos:
        print(f"  - {produto}")

    print("\nProdutos com índice:")

    for indice, produto in enumerate(produtos):
        print(f"  {indice}: {produto}")


# ============================================
# 8. LAÇOS ANINHADOS
# ============================================

def exemplo_lacos_aninhados():
    """
    Simula corredores e prateleiras de um estoque.
    """

    print("\n=== EXEMPLO 8: LAÇOS ANINHADOS ===")

    estoque = [
        ["Teclado", "Mouse", "Cabo"],
        ["Monitor", "Webcam", "Fone"],
        ["Notebook", "Tablet", "Carregador"]
    ]

    print("Mapa do estoque:")

    for corredor in range(len(estoque)):
        print(f"\nCorredor {corredor + 1}:")

        for prateleira in range(len(estoque[corredor])):
            print(
                f"  Prateleira {prateleira + 1}: "
                f"{estoque[corredor][prateleira]}"
            )


# ============================================
# 9. REPETIÇÃO ATÉ CONDIÇÃO SER ATINGIDA
# ============================================

def exemplo_repeticao_validada():
    """
    Simula o cadastro de uma quantidade válida.
    """

    print("\n=== EXEMPLO 9: REPETIÇÃO COM BREAK ===")

    while True:
        quantidade = input(
            "Digite uma quantidade entre 1 e 100: "
        )

        try:
            quantidade = int(quantidade)

            if 1 <= quantidade <= 100:
                break

            print("ERRO: Digite um valor entre 1 e 100.")

        except ValueError:
            print("ERRO: Digite um número inteiro.")

    print(f"Quantidade registrada: {quantidade} unidades.")


# ============================================
# 10. VALIDAÇÃO DE ENTRADA
# ============================================

def exemplo_validacao():
    """
    Demonstra validação de código e quantidade.
    """

    print("\n=== EXEMPLO 10: VALIDAÇÃO DE ENTRADA ===")

    while True:
        try:
            codigo = int(input("Digite o código do produto: "))

            if codigo > 0:
                break

            print("ERRO: O código deve ser maior que zero.")

        except ValueError:
            print("ERRO: Digite um código numérico.")

    quantidade = validar_quantidade(
        "Digite a quantidade disponível: "
    )

    print(f"\nCódigo registrado: {codigo}")
    print(f"Quantidade registrada: {quantidade}")


# ============================================
# 11. MENU PRINCIPAL
# ============================================

def menu_principal():
    """
    Menu interativo com os exemplos de laços.
    """

    print("\n" + "=" * 50)
    print("       SISTEMA DE CONTROLE DE ESTOQUE")
    print("     Demonstração de laços de repetição")
    print("=" * 50)

    while True:
        print("\n" + "-" * 50)
        print("MENU PRINCIPAL")
        print("-" * 50)
        print("1 - Contadora")
        print("2 - Acumuladora")
        print("3 - Flag")
        print("4 - While + If")
        print("5 - Break e Continue")
        print("6 - For com range()")
        print("7 - For com listas")
        print("8 - Laços aninhados")
        print("9 - Repetição com validação")
        print("10 - Validação de entrada")
        print("11 - Registrar produtos")
        print("0 - Sair")

        opcao = validar_opcao(
            "Escolha uma opção: ",
            ["0", "1", "2", "3", "4", "5",
             "6", "7", "8", "9", "10", "11"]
        )

        if opcao == "0":
            print("\nSaindo do sistema...")
            break

        if opcao == "1":
            exemplo_contadora()
        elif opcao == "2":
            exemplo_acumuladora()
        elif opcao == "3":
            exemplo_flag()
        elif opcao == "4":
            exemplo_nivel_estoque()
        elif opcao == "5":
            exemplo_break_continue()
        elif opcao == "6":
            exemplo_for_range()
        elif opcao == "7":
            exemplo_for_listas()
        elif opcao == "8":
            exemplo_lacos_aninhados()
        elif opcao == "9":
            exemplo_repeticao_validada()
        elif opcao == "10":
            exemplo_validacao()
        elif opcao == "11":
            registrar_produtos()

        input("\nPressione Enter para continuar...")


# ============================================
# 12. APLICAÇÃO PRÁTICA
# ============================================

def registrar_produtos():
    """
    Registra produtos e calcula estatísticas do estoque.
    """

    print("\n=== APLICAÇÃO PRÁTICA: ESTOQUE ===")
    print("Digite 'fim' no nome do produto para encerrar.")
    print("-" * 40)

    produtos = []
    total_unidades = 0
    maior_estoque = 0
    produto_maior_estoque = ""

    while True:
        nome = input("Nome do produto: ").strip()

        if nome.lower() == "fim":
            break

        quantidade = validar_quantidade(
            "Quantidade em estoque: "
        )

        produtos.append({
            "nome": nome,
            "quantidade": quantidade
        })

        total_unidades += quantidade

        if quantidade > maior_estoque:
            maior_estoque = quantidade
            produto_maior_estoque = nome

        print(f"Produto '{nome}' registrado com sucesso.")

    if produtos:
        print("\n" + "=" * 40)
        print("RELATÓRIO DO ESTOQUE")
        print("=" * 40)

        for produto in produtos:
            if produto["quantidade"] == 0:
                status = "ESGOTADO"
            elif produto["quantidade"] < 10:
                status = "BAIXO"
            else:
                status = "NORMAL"

            print(
                f"{produto['nome']}: "
                f"{produto['quantidade']} unidades - {status}"
            )

        print("-" * 40)
        print(f"Total de produtos cadastrados: {len(produtos)}")
        print(f"Total de unidades: {total_unidades}")
        print(
            f"Maior estoque: {produto_maior_estoque} "
            f"({maior_estoque} unidades)"
        )
    else:
        print("\nNenhum produto foi cadastrado.")


# ============================================
# 13. EXEMPLO ADICIONAL: TABELA DE PREÇOS
# ============================================

def exemplo_tabela_precos():
    """
    Percorre uma lista e exibe preços simulados.
    """

    print("\n=== EXEMPLO ADICIONAL: TABELA DE PREÇOS ===")

    produtos = {
        "Teclado": 80.00,
        "Mouse": 45.00,
        "Monitor": 650.00,
        "Fone": 120.00
    }

    for nome, preco in produtos.items():
        print(f"{nome}: R$ {preco:.2f}")


# ============================================
# 14. TESTE RÁPIDO
# ============================================

def teste_rapido():
    """
    Executa pequenos exemplos sem abrir o menu completo.
    """

    print("\n=== TESTE RÁPIDO ===")
    print("1 - Conferir prateleiras")
    print("2 - Mostrar produtos")
    print("3 - Mostrar preços")

    opcao = input("Escolha: ")

    if opcao == "1":
        for prateleira in range(1, 6):
            print(f"Prateleira {prateleira}: OK")

    elif opcao == "2":
        produtos = ["Teclado", "Mouse", "Monitor", "Fone"]

        for indice, produto in enumerate(produtos, 1):
            print(f"{indice}. {produto}")

    elif opcao == "3":
        exemplo_tabela_precos()

    else:
        print("Opção inválida!")


# ============================================
# PONTO DE ENTRADA
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("       CONTROLE DE ESTOQUE")
    print("=" * 50)
    print("1 - Menu Principal")
    print("2 - Teste Rápido")
    print("3 - Executar exemplos")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        menu_principal()

    elif opcao == "2":
        teste_rapido()

    elif opcao == "3":
        exemplo_contadora()
        exemplo_acumuladora()
        exemplo_for_range()
        exemplo_for_listas()
        exemplo_lacos_aninhados()
        exemplo_tabela_precos()

    elif opcao == "0":
        print("Saindo...")

    else:
        print("Opção inválida!")
