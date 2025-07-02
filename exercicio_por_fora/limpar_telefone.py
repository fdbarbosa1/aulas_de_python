def limpar_telefone(numero):
    numero = numero.strip().replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
    return numero

print(limpar_telefone(" (11) 91234-5678 "))
print(limpar_telefone(" (11) 91234-5678 "))
print(limpar_telefone("11-91234 5678"))
print(limpar_telefone(" 11912-345678 "))