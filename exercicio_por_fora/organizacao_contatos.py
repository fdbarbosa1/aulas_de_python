def organizar_contatos(lista):
    contatos_limpos = set()  # para guardar só únicos

    for nome, telefone in lista:
        nome_limpo = limpar_nome(nome)
        telefone_limpo = limpar_telefone(telefone)
        contato = (nome_limpo, telefone_limpo)
        contatos_limpos.add(contato)
    
    contatos_lista = list(contatos_limpos)
    contatos_ordenados = sorted(contatos_lista, key=lambda c: c[0])
    return contatos_ordenados

def limpar_nome(nome):
    return nome.strip().capitalize()

def limpar_telefone(numero):
    numero = numero.strip().replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
    return numero

dados = [
    (" Alice ", " 11-91234-5678 "),
    ("bob", "11 91234 5678"),
    ("Alice", "11 91234 5678"),
    ("João", "(11)91234-5678"),
    ("BOB", "11-91234-5678"),
]

print(organizar_contatos(dados))


