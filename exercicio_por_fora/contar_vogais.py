def contar_vogais(texto): 
    texto = texto.lower()
    contador = 0
    vogais = "aeiouáéíóúâêôàãõ"
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

print(contar_vogais("Python é massa"))
print(contar_vogais("FLÁVIO"))
print(contar_vogais("É á é á á ô ê"))