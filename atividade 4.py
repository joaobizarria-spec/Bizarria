"""
ATIVIDADE 4 - CLASSIFICADOR DE RESERVA

Proposta:
Verifica se uma pessoa pode reservar uma sala de estudo
de acordo com sua idade e se possui cadastro na biblioteca.

Regras:
- Menor de 14 anos: reserva não permitida
- 14 anos ou mais COM cadastro: reserva liberada
- 14 anos ou mais SEM cadastro: solicitar cadastro
"""

# ============ ENTRADA DE DADOS ============

while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade < 0:
            print("Idade não pode ser negativa. Tente novamente.")
            continue

        break

    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

while True:
    resposta = input(
        "Você possui cadastro na biblioteca? (sim/nao): "
    ).strip().lower()

    if resposta in ["sim", "s"]:
        possui_cadastro = True
        break

    elif resposta in ["nao", "não", "n"]:
        possui_cadastro = False
        break

    else:
        print("Resposta inválida! Digite 'sim' ou 'nao'.")

# ============ PROCESSAMENTO E CLASSIFICAÇÃO ============

if idade < 14:
    mensagem = "Reserva não permitida"
    status = "negado"

elif idade >= 14 and possui_cadastro:
    mensagem = "Reserva liberada"
    status = "permitido"

else:
    mensagem = "Faça seu cadastro"
    status = "pendente"

# ============ SAÍDA FORMATADA ============

print("\n" + "=" * 50)
print("           RESULTADO DA RESERVA")
print("=" * 50)

print(f"Idade informada:        {idade} anos")
print(f"Possui cadastro:        {'Sim' if possui_cadastro else 'Não'}")
print("-" * 50)
print(f"Status:                 {mensagem.upper()}")

if status == "negado":
    print("Motivo: A idade mínima para reservar é 14 anos.")

elif status == "permitido":
    print("Motivo: Idade e cadastro verificados com sucesso.")

else:
    print("Motivo: É necessário possuir cadastro na biblioteca.")

print("=" * 50)

# ============ TESTES RÁPIDOS ============

print("\n[TESTES RÁPIDOS]")
print("-" * 50)

print("Caso 1 - Idade: 12, Cadastro: Não")
if 12 < 14:
    print("  Resultado: Reserva não permitida ✓")
else:
    print("  Resultado: ERRO no teste!")

print("Caso 2 - Idade: 16, Cadastro: Sim")
if 16 >= 14 and True:
    print("  Resultado: Reserva liberada ✓")
else:
    print("  Resultado: ERRO no teste!")

print("Caso 3 - Idade: 20, Cadastro: Não")
if 20 >= 14 and False:
    print("  Resultado: ERRO no teste!")
else:
    print("  Resultado: Faça seu cadastro ✓")

print("-" * 50)
print("[ESTRUTURA DE SELEÇÃO]")
print("-" * 50)
print("1. if idade < 14:")
print("   -> Bloqueia a reserva para pessoas abaixo da idade mínima.")
print()
print("2. elif idade >= 14 and possui_cadastro:")
print("   -> Libera a reserva quando idade e cadastro estão corretos.")
print()
print("3. else:")
print("   -> Indica que falta realizar o cadastro.")
print()
print("A estrutura if-elif-else permite tratar todos os casos.")
print("-" * 50)
