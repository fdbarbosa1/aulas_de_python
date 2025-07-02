import unicodedata

def remover_acentos(texto):
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

def extrair_mensagem(texto):
    texto = remover_acentos(texto)
    letras = [c for c in texto if c.isalpha()]
    letras_filtradas = []
    for i, letra in enumerate(letras):
        if i % 4 == 0:
            letras_filtradas.append(letra.upper())
    return ''.join(letras_filtradas)

texto = "A senha secreta está no cofre!"
print(extrair_mensagem(texto))  # Deve imprimir AACENF