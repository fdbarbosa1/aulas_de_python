def verificar_senha(senha):
    tem_maiuscula = False
    tem_minuscula = False
    tem_digito = False
    tem_especial = False

    especiais = "!@#$%^&*()-_=+"

    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_digito = True
        elif char in especiais:
            tem_especial = True

    comprimento_ok = len(senha) >= 8

    faltando = []
    if not comprimento_ok:
        faltando.append("mínimo de 8 caracteres")
    if not tem_maiuscula:
        faltando.append("letra maiúscula")
    if not tem_minuscula:
        faltando.append("letra minúscula")
    if not tem_digito:
        faltando.append("dígito")
    if not tem_especial:
        faltando.append("caractere especial")

    if not faltando:
        return "Senha válida."
    else:
        return "Senha inválida: faltam " + ", ".join(faltando) + "."
    

print(verificar_senha("Senha123!"))     # válida
print(verificar_senha("senha123"))      # inválida
print(verificar_senha("12345678"))      # inválida
print(verificar_senha("Abcdefgh"))      # inválida
print(verificar_senha("Abc123!@#"))     # válida
