def filtrar_negativos(lista): 
    negativos = []                     

    for numero in lista:          
        if numero < 0:       
            negativos.append(numero)  

    return negativos                  


print(filtrar_negativos([1, -2, 3, -4, 0, 5]))
print(filtrar_negativos([0, 2, 4, -1])) 
print(filtrar_negativos([5, 10, 15])) 