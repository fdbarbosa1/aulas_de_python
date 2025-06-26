import unicodedata
def eh_palindromo(frase):
    frase = frase.lower()
    frase = remover_acentos(frase)
    frase = ''.join(c for c in frase if c.isalnum())  # remove espaços e pontuação
    frase_invertida = frase[::-1]
    return frase == frase_invertida

def remover_acentos(txt):
    txt_normalizado = unicodedata.normalize('NFD', txt)
    txt_sem_acentos = ''.join(
        c for c in txt_normalizado
        if unicodedata.category(c) != 'Mn'
    )
    return txt_sem_acentos

print(eh_palindromo("ovo"))                         # True
print(eh_palindromo("Ame a ema"))                   # True
print(eh_palindromo("Socorram-me subi no ônibus em Marrocos"))  # True
print(eh_palindromo("Python"))                      # False