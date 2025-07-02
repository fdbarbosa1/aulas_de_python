def decodificar_mensagem(texto):
    caracteres = '$@!#$%&*()?][;.,'
    
    for simbolo in caracteres:
        texto = texto.replace(simbolo, "")
    
    letras = []
    numeros = []
    
    for char in texto:
        if char.isalpha():
            letras.append(char)
        elif char.isdigit():
            numeros.append(char)

    letras_ordenadas = sorted(set(l.lower() for l in letras))
    
    numeros_ordenados = sorted(numeros)
    
    senha = ''.join(letras_ordenadas[:3]) + ''.join(numeros_ordenados[-4:])
    print(senha)


decodificar_mensagem("C0d3#C@a5f9e!")