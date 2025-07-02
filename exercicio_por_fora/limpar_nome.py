def limpar_nome(nome):
    return nome.strip().capitalize()


print(limpar_nome('flávio'))
print(limpar_nome("  FLÁVIO  "))
print(limpar_nome("joÃoZINHO"))
print(limpar_nome(" aNA "))