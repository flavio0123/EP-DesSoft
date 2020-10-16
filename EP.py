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
    especial1 = random.choice(lista)
    especial2 = random.choice(lista)

    jogador = 9
    mesa = carta3 + carta4

    pergunta = input('Você quer apostar ? ') 

    if pergunta == 'nao':
        break

    if pergunta == 'sim':

        x = int(input('Quanto você quer apostar ? '))

        if x <= dinheiros:

            y = input('Você quer apostar em: Jogador, Mesa ou Empate ? ')


            if jogador == 8 or jogador == 9 and y == 'Jogador':
                Ganhou = True

            elif mesa == 8 or mesa == 9 and y == 'Mesa':            
                Ganhou = True

            elif jogador == 8  or jogador == 9 and y != 'Jogador':
                Perdeu = True

            elif mesa == 8 or mesa == 9 and y != 'Mesa':
                Perdeu = True

            else: 

                if jogador >= 10:

                    jogador = jogador % 10
        
                if mesa >= 10:
                    
                    mesa = mesa % 10

                if jogador < 8:

                    if jogador == 6 or jogador == 7:
                            pass
                    
                    if jogador < 6:
                        jogador += especial1

                if mesa < 8:

                    if mesa == 6 or mesa == 7:
                            pass
                    
                    if mesa < 6:
                        mesa += especial2 


                if jogador >= 10:

                    jogador = jogador % 10
        
                if mesa >= 10:
                    
                    mesa = mesa % 10

                if jogador > mesa:
                    if y == 'Jogador':
                        Ganhou = True
                    else:
                        Perdeu = True

                elif mesa > jogador:
                    if y == 'Mesa':
                        Ganhou = True
                    else:
                        Perdeu = True

                elif mesa == jogador:
                    dinheiros += 80
                    
            if Ganhou:
                Ganhou = False
                dinheiros += x
                print('Parábens você ganhou, e agora tem {} dinheiros !'.format(dinheiros))

            if Perdeu:
                Perdeu = False
                dinheiros -= x
                print('Infelizmente você perdeu, e agora tem {} dinheiros'.format(dinheiros))

        else:
             print('Você não tem dinheiro suficiente para fazer essa aposta, seu saldo é de {} dinheiros'.format(dinheiros))

          


