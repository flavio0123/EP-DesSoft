# EP - Design de Software
# Equipe: Flavio Squillante
# Data: 23/09/2020

import random

dinheiros = 100

# lista com os valores das cartas

lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] 

while dinheiros > 0: 

    carta1 = random.choice(lista)
    carta2 = random.choice(lista)
    carta3 = random.choice(lista)
    carta4 = random.choice(lista)





    jogador = carta1 + carta2
    mesa = carta3 + carta4

    pergunta = input('Você quer apostar ? ') 

    if pergunta == 'nao':
        break

    if pergunta == 'sim':

        x = int(input('Quanto você quer apostar ? '))
        y = input('Você quer apostar em: Jogador, Mesa ou Empate ? ')

        if jogador >= 10 or mesa >= 10:
            
            mesa = mesa % 10
            jogador = jogador % 10

        if y == 'Jogador':
            pass

        elif y == 'Empate':
            print(mesa)

          


