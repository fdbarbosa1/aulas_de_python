from collections import Counter
import unicodedata

def contar_palavras_unicas(frase):
    frase = frase.lower()
    frase = remover_acentos(frase)
    palavras = frase.split()
    contagem = Counter(palavras)
    unicas = 0
    for palavra in contagem:
        if contagem[palavra] == 1:
            unicas += 1
    return unicas

def remover_acentos(txt):
    txt_normalizado = unicodedata.normalize('NFD', txt)
    txt_sem_acentos = ''.join(
        c for c in txt_normalizado
        if unicodedata.category(c) != 'Mn'
    )
    return txt_sem_acentos






print(contar_palavras_unicas("eu gosto de python e eu gosto de programar"))


print(contar_palavras_unicas("a casa é bonita e a casa é grande"))
