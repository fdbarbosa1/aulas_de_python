def numero_no_intervalo(n, minimo, maximo):
    if minimo <= n <= maximo :
        return True
    else:
        return False
    
print(numero_no_intervalo(5, 1, 10)) 
print(numero_no_intervalo(20, 10, 15))
print(numero_no_intervalo(0, 1,4))  