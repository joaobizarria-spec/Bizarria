titulo = "Cálculo de ingressos para o cinema"
descricao = "Uma pessoa comprou três ingressos, cada um por: "
cont = " e recebeu um desconto de: "
pergunta = "Quanto ela gastou?"
resposta = "Ela gastou: "

preco = 25.00
quantidade = 3
desconto = 15.00
subtotal = preco * quantidade
valor_final = subtotal - desconto
# .2f formata os valores com 2 casas decimais

print(f"""
{titulo}
{descricao}R$ {preco:.2f}{cont}R$ {desconto:.2f}

{pergunta}
{resposta}R$ {valor_final:.2f}

""")
