

def contar_nomes(frase):
    frase = frase.replace(".", "").replace(",", "") 
    contagem = {}
    for palavra in frase.split():
        if palavra[0].isupper():
            nome = palavra.strip(".,").capitalize()
            contagem[nome] = contagem.get(nome, 0) + 1
    return contagem




texto = "João foi ao mercado. Maria ficou em casa. João voltou às 18h. MARIA saiu às 19h."
print(contar_nomes(texto))



