def somar_positivos(lista):
    soma = 0
    for numero in lista:
        if numero > 0:
            soma += numero
    return soma


print(somar_positivos([1, -2, 3, -4, 5]) )   
print(somar_positivos([-1, -2, -3]) )       
print(somar_positivos([10, 20, 30]))  