def mover_robo(comandos):
    linha = 0
    coluna = 0
    for comando in comandos:
        if comando == "C":
            linha -= 1
        elif comando == "B":
            linha += 1
        elif comando == "D":
            coluna += 1
        elif comando == "E":
            coluna -= 1
        if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
            return "Fora da grade!"
    return (linha, coluna)

print(mover_robo("DDDBBBEE"))   # ➜ (3,1)
print(mover_robo("BBBBB"))      # ➜ Fora da grade!
print(mover_robo("CDCDCD"))     # ➜ Fora da grade!