"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome  ")
idade = input("Digite sua idade  ")

if nome and idade:


    print (f"seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")

    if '' in nome:
        print ("seu nome contem espaços ")
    else:
        print("seu nome não contem espaços ")
        
    numero_de_letras = len(nome)
    print(f"quantidade de letras em seu nome : {numero_de_letras}")
    print(f"a primeira letra do seu nome é {nome[0]}")
    print(f"a primeira letra do seu nome é {nome[-1]}")

else:
    print ("digite novamente !")
    

 


