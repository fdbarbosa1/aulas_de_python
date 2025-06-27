def espelhar_frase(frase):
    palavras = frase.split()
    palavras_espelhadas = [p[::-1] for p in palavras]
    linha_espelhada = ' '.join(palavras_espelhadas)
    print(frase)
    print(linha_espelhada)

espelhar_frase("o céu é lindo")