# EP - Design de Software
# Equipe: Flavio Squillante
# Data: 23/09/2020

import random

dinheiros = 100

# lista com os valores das cartas

baralho = 4 * [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] 

pergunta = input('Você quer apostar ? ') 

while dinheiros > 0: 
   
    Ganhou = False

    Perdeu = False

    if pergunta == 'sim':

        pergunta2 = input('O jogo será realizado com quantos baralhos ? (1,6,8): ')

        x = int(input('Quanto você quer apostar ? '))

        if pergunta2 == '1':

            carta1 = random.choice(baralho)
            carta2 = random.choice(baralho)
            carta3 = random.choice(baralho)
            carta4 = random.choice(baralho)
            especial1 = random.choice(baralho)
            especial2 = random.choice(baralho)
        
        if pergunta2 == '6':

            baralho = baralho * 6

            carta1 = random.choice(baralho)
            carta2 = random.choice(baralho)
            carta3 = random.choice(baralho)
            carta4 = random.choice(baralho)
            especial1 = random.choice(baralho)
            especial2 = random.choice(baralho)

        if pergunta2 == '8':

            baralho = baralho * 8

            carta1 = random.choice(baralho)
            carta2 = random.choice(baralho)
            carta3 = random.choice(baralho)
            carta4 = random.choice(baralho)
            especial1 = random.choice(baralho)
            especial2 = random.choice(baralho)  

        jogador = carta1 + carta2
        mesa    = carta3 + carta4

        if x <= dinheiros:

            y = input('Você quer apostar em: Jogador, Mesa ou Empate ? ')

            print('A soma inicial das cartas do jogador era {0} , equanto a da mesa era {1}'.format(jogador,mesa))

            if jogador == 8 and y == 'Jogador' or jogador == 9 and y == 'Jogador':

                dinheiros += x
                Ganhou = True  

            elif mesa == 8 and y == 'Mesa' or mesa == 9 and y == 'Mesa':            

                dinheiros += int(x * 0.95)
                Ganhou = True

            elif jogador == 8 and y != 'Jogador' or jogador == 9 and y != 'Jogador':

                dinheiros -= x
                Perdeu = True
                    
            elif mesa == 8 and y != 'Mesa' or mesa == 9 and y != 'Mesa':

                dinheiros -= x
                Perdeu = True

            else: 

                if jogador >= 10:

                    jogador = jogador % 10
        
                elif mesa >= 10:
                    
                    mesa = mesa % 10

                elif jogador == 6 or jogador == 7 or mesa == 6 or mesa == 7:
                      
                    pass
            
                elif jogador < 6 or mesa < 6:

                    if jogador < 6:
                            
                        jogador += especial1

                        print('A terceira carta do jogador foi {}'.format(especial1))

                        if jogador >= 10:

                            jogador = jogador % 10

                    if mesa < 6:

                        mesa += especial2 

                        print('A terceira carta da mesa foi {}'.format(especial2))

                        if mesa >= 10:
                        
                            mesa = mesa % 10

                    print('A soma final das cartas do jogador era {0} , equanto a da mesa era {1}'.format(jogador,mesa))   

                elif jogador > mesa:

                    if y == 'Jogador':

                        dinheiros += x
                        Ganhou = True

                    else:

                        dinheiros -= x
                        Perdeu = True
                
                elif mesa > jogador:

                    if y == 'Mesa':

                        dinheiros += int(x * 0.95)
                        Ganhou = True                         
                    
                    else:
                        dinheiros -= x
                        Perdeu = True

                elif mesa == jogador:

                    if y == 'Empate':

                        dinheiros += x * 8
                        Ganhou = True 

                    else:

                        dinheiros -= x
                        Perdeu = True

            if Ganhou:
                
                print('Parábens você ganhou, e agora tem {} dinheiros !'.format(dinheiros)) 

            if Perdeu:

                print('Infelizmente você perdeu, e agora tem {} dinheiros'.format(dinheiros))
                             
            if dinheiros == 0:

                print('O jogo acabou devido o seu saldo estar zerado, obrigado por jogar !')
            
            else:
        
                pergunta = input('Essa partida acabou, gostaria de apostar novamente ? ')
  
        else:
            
            print('Você não tem dinheiro suficiente para fazer essa aposta, seu saldo é de {} dinheiros'.format(dinheiros))

    else:

        print('Obrigado por Jogar, você terminou com o saldo de {} dinheiros !'.format(dinheiros))

        break
