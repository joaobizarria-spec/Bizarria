valor_veiculo = float(input("Digite o valor do veículo (R$): "))
percentual_seguro = float(input("Digite o percentual do seguro (%): "))
meses = int(input("Digite a quantidade de meses: "))

valor_seguro = valor_veiculo * (percentual_seguro / 100)
valor_total = valor_seguro * meses

print(f"O valor mensal do seguro será de R$ {valor_seguro:.2f}")
print(f"O valor total em {meses} meses será de R$ {valor_total:.2f}")