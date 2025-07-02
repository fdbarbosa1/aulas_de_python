import string
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

texto = "Você é um Idiota e muito feio."
palavras_proibidas = ["idiota", "feio"]

resultado = censurar_texto(texto, palavras_proibidas)
print (resultado)