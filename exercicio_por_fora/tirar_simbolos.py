import unicodedata

def limpar_texto(texto):
    # Remove acentos
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join([char for char in texto if unicodedata.category(char) != 'Mn'])
    
    # Define os símbolos que serão removidos
    caracteres = '$@!#$%&*()?][;.,'
    for simbolo in caracteres:
        texto = texto.replace(simbolo, "")
    
    return texto

