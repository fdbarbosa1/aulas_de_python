def filtrar_pares(lista):          # Definimos uma função chamada filtrar_pares, que recebe uma lista
    pares = []                     # Criamos uma lista vazia para guardar os números pares

    for numero in lista:          # Para cada número dentro da lista que recebemos...
        if numero % 2 == 0:       # Se o número dividido por 2 tiver resto zero (ou seja, for par)...
            pares.append(numero)  # Adicionamos esse número na lista de pares

    return pares                  # Retornamos a lista de pares no final


print(filtrar_pares([1, 2, 3, 4, 5, 6]))  # ➜ Deve imprimir [2, 4, 6]
print(filtrar_pares([10, 15, 22]))       # ➜ Deve imprimir [10, 22]
