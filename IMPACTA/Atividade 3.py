def pode_entrar(pessoa):
    return (pessoa["ingresso_valido"] and pessoa["cadastro_ativo"]) or pessoa["organizador"]


pessoa = {
    "ingresso_valido": True,
    "cadastro_ativo": True,
    "organizador": False
}

print(pode_entrar(pessoa))