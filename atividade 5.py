"""
ATIVIDADE 5 - SISTEMA DE PEDIDOS DE UMA LANCHONETE

Proposta:
Demonstra estruturas de seleção utilizando um sistema simples
para avaliar pedidos, classificar valores e escolher opções.

Conceitos utilizados:
- if aninhado
- if/elif/else
- match/case
- match/case com guarda
- menu interativo
- funções
- listas
"""

# ============================================
# 1. ESTRUTURA ANINHADA
# ============================================

def verificar_entrega():
    """
    Verifica se um pedido pode receber entrega grátis.
    """

    print("\n=== VERIFICAÇÃO DE ENTREGA ===")

    valor = float(input("Digite o valor do pedido: R$ "))
    distancia = float(input("Digite a distância em km: "))

    print(f"Pedido: R$ {valor:.2f} - Distância: {distancia:.1f} km")

    if valor >= 80:
        print("Valor suficiente para avaliar a entrega.")

        if distancia <= 5:
            print("RESULTADO: ENTREGA GRÁTIS")
        else:
            print("RESULTADO: ENTREGA COM TAXA - distância acima de 5 km")
    else:
        print("RESULTADO: ENTREGA COM TAXA - pedido abaixo de R$ 80,00")


# ============================================
# 2. ESTRUTURA ENCADEADA COM ELIF
# ============================================

def classificar_pedido():
    """
    Classifica o pedido de acordo com seu valor.
    """

    print("\n=== CLASSIFICAÇÃO DO PEDIDO ===")

    valor = float(input("Digite o valor do pedido: R$ "))

    if valor >= 150:
        classificacao = "PEDIDO ESPECIAL"
    elif valor >= 100:
        classificacao = "PEDIDO GRANDE"
    elif valor >= 50:
        classificacao = "PEDIDO MÉDIO"
    elif valor > 0:
        classificacao = "PEDIDO PEQUENO"
    else:
        classificacao = "VALOR INVÁLIDO"

    print(f"Valor: R$ {valor:.2f}")
    print(f"Classificação: {classificacao}")


# ============================================
# 3. ESTRUTURA MATCH CASE
# ============================================

def escolher_categoria():
    """
    Processa a categoria escolhida pelo cliente.
    """

    print("\n=== CATEGORIAS DA LANCHONETE ===")
    print("1 - Hambúrgueres")
    print("2 - Pizzas")
    print("3 - Bebidas")
    print("4 - Sobremesas")
    print("0 - Voltar")

    opcao = input("Digite a opção desejada: ").strip().lower()

    match opcao:
        case "1":
            print("Categoria escolhida: HAMBÚRGUERES")
        case "2":
            print("Categoria escolhida: PIZZAS")
        case "3":
            print("Categoria escolhida: BEBIDAS")
        case "4":
            print("Categoria escolhida: SOBREMESAS")
        case "0" | "voltar":
            print("Voltando ao menu...")
        case _:
            print(f"OPÇÃO INVÁLIDA: {opcao}")


# ============================================
# 4. MATCH CASE COM GUARDA
# ============================================

def avaliar_cliente():
    """
    Define um benefício de acordo com o valor gasto
    e a quantidade de pedidos realizados.
    """

    print("\n=== AVALIAÇÃO DO CLIENTE ===")

    nome = input("Digite o nome do cliente: ")
    valor = float(input("Digite o valor da compra: R$ "))
    pedidos = int(input("Digite a quantidade de pedidos anteriores: "))

    dados = (valor, pedidos)

    print(f"\nCliente: {nome}")
    print(f"Compra atual: R$ {valor:.2f}")
    print(f"Pedidos anteriores: {pedidos}")

    match dados:
        case (v, p) if v >= 200 and p >= 5:
            print(f"{nome}: CLIENTE VIP - recebeu 15% de desconto")

        case (v, p) if v >= 100 and p >= 3:
            print(f"{nome}: CLIENTE FREQUENTE - recebeu 10% de desconto")

        case (v, p) if v >= 50:
            print(f"{nome}: CLIENTE REGULAR - recebeu 5% de desconto")

        case (v, _) if v > 0:
            print(f"{nome}: COMPRA REGISTRADA - sem desconto")

        case _:
            print(f"{nome}: DADOS INVÁLIDOS")


# ============================================
# 5. FUNÇÃO PRINCIPAL COM MENU INTERATIVO
# ============================================

def menu_principal():
    """
    Menu interativo para acessar as diferentes estruturas.
    """

    print("=" * 50)
    print("        SISTEMA DA LANCHONETE")
    print("Demonstração de estruturas de seleção")
    print("=" * 50)

    while True:
        print("\n" + "-" * 50)
        print("MENU PRINCIPAL")
        print("-" * 50)
        print("1 - Verificar Entrega")
        print("2 - Classificar Pedido")
        print("3 - Escolher Categoria")
        print("4 - Avaliar Cliente")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == "1":
            verificar_entrega()

        elif opcao == "2":
            classificar_pedido()

        elif opcao == "3":
            escolher_categoria()

        elif opcao == "4":
            avaliar_cliente()

        elif opcao == "5":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\nOPÇÃO INVÁLIDA! Tente novamente.")

        input("\nPressione Enter para continuar...")


# ============================================
# 6. FUNÇÕES ADICIONAIS COM REPETIÇÃO
# ============================================

def cadastrar_varios_pedidos():
    """
    Registra vários pedidos utilizando uma lista.
    """

    print("\n=== CADASTRO DE PEDIDOS ===")

    pedidos = []
    continuar = "s"

    while continuar.lower() == "s":
        print("\n" + "-" * 30)

        cliente = input("Nome do cliente: ")
        valor = float(input("Valor do pedido: R$ "))

        pedidos.append({
            "cliente": cliente,
            "valor": valor
        })

        continuar = input("Adicionar outro pedido? (s/n): ")

    if pedidos:
        print("\nRESULTADOS DOS PEDIDOS")
        print("-" * 30)

        for pedido in pedidos:
            valor = pedido["valor"]

            if valor >= 150:
                status = "ESPECIAL"
            elif valor >= 100:
                status = "GRANDE"
            elif valor >= 50:
                status = "MÉDIO"
            else:
                status = "PEQUENO"

            print(
                f"{pedido['cliente']}: "
                f"R$ {valor:.2f} - {status}"
            )


# ============================================
# 7. MENU AVANÇADO
# ============================================

def menu_avancado():
    """
    Menu usando match/case.
    """

    print("=" * 50)
    print("      LANCHONETE - MENU AVANÇADO")
    print("=" * 50)

    while True:
        print("\n1 - Verificar Entrega")
        print("2 - Classificar Pedido")
        print("3 - Escolher Categoria")
        print("4 - Avaliar Cliente")
        print("5 - Cadastrar Vários Pedidos")
        print("6 - Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                verificar_entrega()
            case "2":
                classificar_pedido()
            case "3":
                escolher_categoria()
            case "4":
                avaliar_cliente()
            case "5":
                cadastrar_varios_pedidos()
            case "6" | "sair":
                print("\nSaindo do sistema...")
                break
            case _:
                print("\nOPÇÃO INVÁLIDA!")

        if opcao not in ["6", "sair"]:
            input("\nPressione Enter para continuar...")


# ============================================
# 8. TESTE RÁPIDO
# ============================================

def teste_rapido():
    """
    Permite testar rapidamente algumas funcionalidades.
    """

    print("\n=== TESTE RÁPIDO ===")
    print("1 - Classificar pedido")
    print("2 - Escolher categoria")
    print("3 - Cadastrar pedidos")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        classificar_pedido()
    elif opcao == "2":
        escolher_categoria()
    elif opcao == "3":
        cadastrar_varios_pedidos()
    else:
        print("Opção inválida!")


# ============================================
# PONTO DE ENTRADA
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("      SISTEMA DA LANCHONETE")
    print("=" * 50)
    print("1 - Menu Principal")
    print("2 - Menu Avançado")
    print("3 - Teste Rápido")
    print("4 - Sair")

    versao = input("\nEscolha uma versão (1-4): ")

    if versao == "1":
        menu_principal()
    elif versao == "2":
        menu_avancado()
    elif versao == "3":
        teste_rapido()
    elif versao == "4":
        print("Saindo...")
    else:
        print("Opção inválida!")
