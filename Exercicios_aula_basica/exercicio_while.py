"""
Iterando strings com while
"""
#       012345678910
# nome = 'Flavio Dantas'  # Iteráveis
#      1110987654321


nome = 'isadora Coradim'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    
    novo_nome += f'*{letra}'
    print (novo_nome)
    indice += 1

novo_nome += '*'
print(novo_nome)
