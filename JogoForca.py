import os
des_forca = ['''
 +---+
 |   |
     |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |    
=========
''']

print('* Jogo da Forca *')
#LISTAS DAS CATEGORIAS
capitais = ["berlim","pequim","lisboa","lima","camberra"]
animais = ['Leao','vaca','cachorro','mamute','esquilo']
frutas = ['banana','abacate','laranja','abacaxi','melancia']
cursos = ["informatica","farmacia","fisioterapia","medicina","mecatronica"]
marcas = ["toyota","ford","volkswagem","chevrolet","bugatti"]
cor = ["amarelo","vermelho","verde","laranja","ciano"]
import random
op=0
aux = 0
usada = []
while op!=7:
    usada.clear()
    i=0
    print("Vamos brincar de forca? \n")
    op = int(input(("Escolha uma das opções: \n 1-Capitais\n2-Frutas\n3-Animais\n4-Cursos\n5-Marcas de carros\n6-Cor\n7-Sair\n")))
    if op==1:
        sorteio = random.choice(capitais)
        lista = []  # lista auxiliar
        tam = len(sorteio)  # Ve o tamanho da palavra sorteada
        for j in range(0, tam,1):  # Salva em uma lista auxiliar caracteres para completar o tamanho esquivalente a palavra
           lista.append("?")
        while i < 6:  # Verifica se a lista de boneco esta no final
            rep = 1
            while rep == 1:
                print(f"{des_forca[i]}")
                print(lista)
                print(f"\nNumeros digitados : {usada}")
                resp = input("Digite uma letra: \n").lower()
                cont = 0
                for j in range(0, tam, 1):
                    if resp == sorteio[j]:  # Se for encontrado, adiciona na lista auxiliar
                        lista[j] = resp
                    else:  # Se nao achou, adiciona ao contador
                        cont = cont + 1
                if cont == tam:  # Se contador for igual ao tamanho, é porque nao achou na palavra, logo não foi encontrado
                    print("Letra não encontrada!")
                    usada.append(resp)
                    aux = aux + 1
                    i = i + 1
                    rep = 0
                else:
                    usada.append(resp)
                    aux = aux + 1
                    print("Letra encontrada!")
                    rep = 1
                cont2 = 0
                for j in range (0,tam,1):
                    if lista[j] == sorteio[j]:
                        cont2 = cont2 +1
                if cont2 == tam:
                    rep=0
                    i=7
        if cont2 == tam:
            print("\n\n\nParabens ! Você completou a palavra : ",sorteio.upper())
            print("\n\n\n")
        else:
            print("\n\n\nNão foi dessa vez!")
            print("A palavra era : ", sorteio.upper())
            print("\n\n\n\n\n\n")

    elif op == 2:
        sorteio = random.choice(animais)
        lista = []  # lista auxiliar
        tam = len(sorteio)  # Ve o tamanho da palavra sorteada
        for j in range(0, tam,1):  # Salva em uma lista auxiliar caracteres para completar o tamanho esquivalente a palavra
           lista.append("?")
        while i < 6:  # Verifica se a lista de boneco esta no final
            rep = 1
            while rep == 1:
                print(f"{des_forca[i]}")
                print(lista)
                print(f"\nNumeros digitados : {usada}")
                resp = input("Digite uma letra: \n").lower()
                cont = 0
                for j in range(0, tam, 1):
                    if resp == sorteio[j]:  # Se for encontrado, adiciona na lista auxiliar
                        lista[j] = resp
                    else:  # Se nao achou, adiciona ao contador
                        cont = cont + 1
                if cont == tam:  # Se contador for igual ao tamanho, é porque nao achou na palavra, logo não foi encontrado
                    print("Letra não encontrada!")
                    usada.append(resp)
                    aux = aux + 1
                    i = i + 1
                    rep = 0
                else:
                    print("Letra encontrada!")
                    usada.append(resp)
                    aux = aux + 1
                    rep = 1
                cont2 = 0
                for j in range (0,tam,1):
                    if lista[j] == sorteio[j]:
                        cont2 = cont2 +1
                if cont2 == tam:
                    rep=0
                    i=7
        if cont2 == tam:
            print("\n\n\nParabens ! Você completou a palavra : ",sorteio.upper())
            print("\n\n\n")
        else:
            print("\n\n\nNão foi dessa vez!")
            print("A palavra era : ", sorteio.upper())
            print("\n\n\n\n\n\n")
    elif op == 3:
        sorteio = random.choice(frutas)
        lista = []  # lista auxiliar
        tam = len(sorteio)  # Ve o tamanho da palavra sorteada
        for j in range(0, tam,1):  # Salva em uma lista auxiliar caracteres para completar o tamanho esquivalente a palavra
           lista.append("?")
        while i < 6:  # Verifica se a lista de boneco esta no final
            rep = 1
            while rep == 1:
                print(f"{des_forca[i]}")
                print(lista)
                print(f"\nNumeros digitados : {usada}")
                resp = input("Digite uma letra: \n").lower()
                cont = 0
                for j in range(0, tam, 1):
                    if resp == sorteio[j]:  # Se for encontrado, adiciona na lista auxiliar
                        lista[j] = resp
                    else:  # Se nao achou, adiciona ao contador
                        cont = cont + 1
                if cont == tam:  # Se contador for igual ao tamanho, é porque nao achou na palavra, logo não foi encontrado
                    print("Letra não encontrada!")
                    usada.append(resp)
                    aux = aux + 1
                    i = i + 1
                    rep = 0
                else:
                    print("Letra encontrada!")
                    usada.append(resp)
                    aux = aux + 1
                    rep = 1
                cont2 = 0
                for j in range (0,tam,1):
                    if lista[j] == sorteio[j]:
                        cont2 = cont2 +1
                if cont2 == tam:
                    rep=0
                    i=7
        if cont2 == tam:
            print("\n\n\nParabens ! Você completou a palavra : ",sorteio.upper())
            print("\n\n\n")
        else:
            print("\n\n\nNão foi dessa vez!")
            print("A palavra era : ", sorteio.upper())
            print("\n\n\n\n\n\n")

    elif op == 4:
        sorteio = random.choice(cursos)
        lista = []  # lista auxiliar
        tam = len(sorteio)  # Ve o tamanho da palavra sorteada
        for j in range(0, tam,1):  # Salva em uma lista auxiliar caracteres para completar o tamanho esquivalente a palavra
           lista.append("?")
        while i < 6:  # Verifica se a lista de boneco esta no final
            rep = 1
            while rep == 1:
                print(f"{des_forca[i]}")
                print(lista)
                print(f"\nNumeros digitados : {usada}")
                resp = input("Digite uma letra: \n").lower()
                cont = 0
                for j in range(0, tam, 1):
                    if resp == sorteio[j]:  # Se for encontrado, adiciona na lista auxiliar
                        lista[j] = resp
                    else:  # Se nao achou, adiciona ao contador
                        cont = cont + 1
                if cont == tam:  # Se contador for igual ao tamanho, é porque nao achou na palavra, logo não foi encontrado
                    print("Letra não encontrada!")
                    usada.append(resp)
                    aux = aux + 1
                    i = i + 1
                    rep = 0
                else:
                    print("Letra encontrada!")
                    usada.append(resp)
                    aux = aux + 1
                    rep = 1
                cont2 = 0
                for j in range (0,tam,1):
                    if lista[j] == sorteio[j]:
                        cont2 = cont2 +1
                if cont2 == tam:
                    rep=0
                    i=7
        if cont2 == tam:
            print("\n\n\nParabens ! Você completou a palavra : ",sorteio.upper())
            print("\n\n\n")
        else:
            print("\n\n\nNão foi dessa vez!")
            print("A palavra era : ", sorteio.upper())
            print("\n\n\n\n\n\n")

    elif op == 5:
        sorteio = random.choice(marcas)
        lista = []  # lista auxiliar
        tam = len(sorteio)  # Ve o tamanho da palavra sorteada
        for j in range(0, tam,1):  # Salva em uma lista auxiliar caracteres para completar o tamanho esquivalente a palavra
           lista.append("?")
        while i < 6:  # Verifica se a lista de boneco esta no final
            rep = 1
            while rep == 1:
                print(f"{des_forca[i]}")
                print(lista)
                print(f"\nNumeros digitados : {usada}")
                resp = input("Digite uma letra: \n").lower()
                cont = 0
                for j in range(0, tam, 1):
                    if resp == sorteio[j]:  # Se for encontrado, adiciona na lista auxiliar
                        lista[j] = resp
                    else:  # Se nao achou, adiciona ao contador
                        cont = cont + 1
                if cont == tam:  # Se contador for igual ao tamanho, é porque nao achou na palavra, logo não foi encontrado
                    print("Letra não encontrada!")
                    usada.append(resp)
                    aux = aux + 1
                    i = i + 1
                    rep = 0
                else:
                    print("Letra encontrada!")
                    usada.append(resp)
                    aux = aux + 1
                    rep = 1
                cont2 = 0
                for j in range (0,tam,1):
                    if lista[j] == sorteio[j]:
                        cont2 = cont2 +1
                if cont2 == tam:
                    rep=0
                    i=7
        if cont2 == tam:
            print("\n\n\nParabens ! Você completou a palavra : ",sorteio.upper())
            print("\n\n\n")
        else:
            print("\n\n\nNão foi dessa vez!")
            print("A palavra era : ", sorteio.upper())
            print("\n\n\n\n\n\n")
    elif op == 6:
        sorteio = random.choice(cor)
        lista = []  # lista auxiliar
        tam = len(sorteio)  # Ve o tamanho da palavra sorteada
        for j in range(0, tam,1):  # Salva em uma lista auxiliar caracteres para completar o tamanho esquivalente a palavra
           lista.append("?")
        while i < 6:  # Verifica se a lista de boneco esta no final
            rep = 1
            while rep == 1:
                print(f"{des_forca[i]}")
                print(lista)
                print(f"\nNumeros digitados : {usada}")
                resp = input("Digite uma letra: \n").lower()
                cont = 0
                for j in range(0, tam, 1):
                    if resp == sorteio[j]:  # Se for encontrado, adiciona na lista auxiliar
                        lista[j] = resp
                    else:  # Se nao achou, adiciona ao contador
                        cont = cont + 1
                if cont == tam:  # Se contador for igual ao tamanho, é porque nao achou na palavra, logo não foi encontrado
                    print("Letra não encontrada!")
                    usada.append(resp)
                    aux = aux + 1
                    i = i + 1
                    rep = 0
                else:
                    print("Letra encontrada!")
                    usada.append(resp)
                    aux = aux + 1
                    rep = 1
                cont2 = 0
                for j in range (0,tam,1):
                    if lista[j] == sorteio[j]:
                        cont2 = cont2 +1
                if cont2 == tam:
                    rep=0
                    i=7
        if cont2 == tam:
            print("\n\n\nParabens ! Você completou a palavra : ",sorteio.upper())
            print("\n\n\n")
        else:
            print("\n\n\nNão foi dessa vez!")
            print("A palavra era : ", sorteio.upper())
            print("\n\n\n\n\n\n")

    if op < 1 or op > 7:
        op=7;
print("Jogo finalizado! Obrigado por jogar :D ")
