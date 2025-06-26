def filtrar_impares(lista):         
    impares = []                     

    for numero in lista:          
        if numero % 2 != 0:       
            impares.append(numero)  

    return impares   

print(filtrar_impares([1, 2, 3, 4, 5, 6]))  # ➜ [1, 3, 5]
print(filtrar_impares([8, 10, 12, 13, 15])) # ➜ [13, 15]

