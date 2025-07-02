import unicodedata
import string
def filtrar_pares(lista):
    return [n for n in lista if n % 2 == 0]     

def contar_vogais(texto):
    vogais = "aeiouáéíóúâêôàãõ"
    return sum(1 for c in texto.lower() if c in vogais)    


def eh_palindromo(frase):
    # (supondo remover_acentos já disponível)
    f = remover_acentos(frase.lower())
    f = ''.join(c for c in f if c.isalnum())
    return f == f[::-1]

def remover_acentos(txt):
    txt_normalizado = unicodedata.normalize('NFD', txt)
    txt_sem_acentos = ''.join(
        c for c in txt_normalizado
        if unicodedata.category(c) != 'Mn'
    )
    return txt_sem_acentos   


def censurar_texto(texto, palavras_proibidas):

    palavras_censuradas = []

    for palavra in texto.split():
        palavra_limpa = palavra.lower().strip(string.punctuation)
        if palavra_limpa in palavras_proibidas:
            palavras_censuradas.append('***')
        else:
            palavras_censuradas.append(palavra)
    texto_limpo = ' '.join(palavras_censuradas)
    return texto_limpo  


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

ferramentas = {
    "1": ("Filtrar Pares", filtrar_pares),
    "2": ("Contar Vogais", contar_vogais),
    "3": ("Palíndromo", eh_palindromo),
    "4": ("Organizar Contatos", organizar_contatos),
    "5": ("Censurar Texto", censurar_texto),
}

while True:
    print("\n=== Caixa de Ferramentas Python ===")
    for key, (nome, _) in ferramentas.items():
        print(f"{key}. {nome}")
    print("0. Sair")

    escolha = input("Escolha uma opção: ").strip()
    if escolha == "0":
        break

    if escolha not in ferramentas:
        print("Opção inválida!")
        continue

    nome, func = ferramentas[escolha]
    print(f"\n>> Você escolheu: {nome}")

    # Ler argumentos conforme a função
    if escolha == "1":  # Filtrar Pares
        dados = input("Digite números separados por espaço: ")
        lista = [int(x) for x in dados.split()]
        resultado = func(lista)

    elif escolha == "2":  # Contar Vogais
        texto = input("Digite um texto: ")
        resultado = func(texto)

    elif escolha == "3":  # Palíndromo
        frase = input("Digite uma frase: ")
        resultado = func(frase)

    elif escolha == "4":  # Organizar Contatos
        # para simplificar, vamos usar um exemplo fixo ou
        # pedir ao usuário um JSON simples
        import json
        raw = input("Digite lista de contatos JSON: ")
        try:
            lista_contatos = json.loads(raw)
        except json.JSONDecodeError:
            print("JSON inválido! Use o formato: [[\"Nome\",\"Telefone\"], …]")
            continue

        resultado = func(lista_contatos)

    elif escolha == "5":  # Censurar Texto
        texto = input("Digite um texto: ")
        proibidas = input("Palavras proibidas (sep. por vírgula): ").split(",")
        proibidas = [p.strip() for p in proibidas]
        resultado = func(texto, proibidas)

    print(f"\nResultado de '{nome}':\n{resultado}")




