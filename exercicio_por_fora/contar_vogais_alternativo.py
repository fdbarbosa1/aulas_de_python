import unicodedata

def remover_acentos(txt):
    txt_normalizado = unicodedata.normalize('NFD', txt)
    txt_sem_acentos = ''.join(
        c for c in txt_normalizado
        if unicodedata.category(c) != 'Mn'
    )
    return txt_sem_acentos

def contar_vogais(texto):
    texto = remover_acentos(texto.lower()) 
    contador = 0
    vogais = "aeiou"
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

print(contar_vogais("Python é massa"))    
print(contar_vogais("FLÁVIO"))            
print(contar_vogais("É á é á á ô ê"))   
