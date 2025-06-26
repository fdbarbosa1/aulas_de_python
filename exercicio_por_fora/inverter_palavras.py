def inverter_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = palavras[::-1]
    frase_invertida = ' '.join(palavras_invertidas)
    return frase_invertida





print(inverter_palavras("eu gosto de python"))

