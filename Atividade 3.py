print("=" * 50)
print(" SISTEMA DE CINEMA")
print("=" * 50)

nome_cliente = input("Nome do cliente: ")
filme = input("Nome do filme: ")
preco = float(input("Preço do ingresso (R$): "))
quantidade = int(input("Quantidade de ingressos: "))
percentual_desconto = float(input("Percentual de desconto (%): "))

subtotal = preco * quantidade

valor_desconto = subtotal * (percentual_desconto / 100)

total_final = subtotal - valor_desconto

valor_medio = total_final / quantidade

print("\n" + "=" * 50)
print(" RESUMO DA COMPRA")
print("=" * 50)

print(f"Cliente: {nome_cliente}")
print(f"Filme: {filme}")
print(f"Quantidade: {quantidade} ingresso(s)")
print(f"Preço unitário: R$ {preco:.2f}")

print("-" * 50)

print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: {percentual_desconto:.0f}% (R$ {valor_desconto:.2f})")

print("-" * 50)

print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
print(f"\nValor médio por ingresso: R$ {valor_medio:.2f}")

print("\n" + "=" * 50)
print(" OBRIGADO PELA COMPRA!")
print("=" * 50)

print("Processando dados", end="... ")
print("Finalizado!", end="\n\n")
