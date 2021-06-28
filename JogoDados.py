                        #Criar programa onde:
#~> 4 jogadores participem e tenham resultados aleatórios
#~> Opção de quantos lances de dados querem fazer, e guardar os resultados das rodadas em um dict.
#~> Ordenar o dict onde será informado qual jogador venceu mais rodadas, sendo o grande campeão.

print('''
                        Jogo 🎲🎲🎲 Dados
                     🎲🎲🎲🎲 dos 🎲🎲🎲🎲
''') #animação em emoji de dados para animar o jogo em reprodução(copy/paste)simples.
#vou fazer as importações que permitirão a execução do jogo:
from random import randint #Random para que os dados sejam lançados aleatóriamente.
import operator #Operator para ordenar os dicionarios em ordem e por valor das chaves.
from time import sleep #Sleep para que haja uma pausa entre as animações e/ou resultados do jogo.

#Em rodadas os jogadores decidiram quantos lances de dados querem fazer.
rodada = int(input('Quantas vezes você quer lançar os dados? '))
sleep(1)
placar = list() #As listas recebem dicionários.
jogador1 = jogador2 = jogador3 = jogador4 = 0 #Aqui vão ser exibidos os resultados das partidas.
empates = jogador1 = jogador2 = jogador3 = jogador4 != 0
print('Iniciando a partida!')
sleep(.5)
print('  🎲 ')
sleep(.5)
print(' 🎲🎲')
sleep(.5)
print('🎲🎲🎲')
sleep(.5)
for r in range(rodada):
    rodada = dict() #Aqui ficarão armazenadas as informações de cada partida.
    rodada =  {'jogador1': randint(1, 6),
               'jogador2': randint(1, 6), #~> Randint fará a aleatoridade dos lances.
               'jogador3': randint(1, 6),
               'jogador4': randint(1, 6),}
    sleep(1)
    print(f'{r + 1}º rodada: {rodada}')
    sleep(1)
    if  (rodada['jogador3'] < rodada['jogador1'] > rodada['jogador2']) and rodada['jogador1'] > rodada['jogador4']:
         jogador1+=1
    elif(rodada['jogador3'] < rodada['jogador2'] > rodada['jogador1']) and rodada['jogador2'] > rodada['jogador4']:
         jogador2+=1
    elif(rodada['jogador2'] < rodada['jogador3'] > rodada['jogador1']) and rodada['jogador3'] > rodada['jogador4']:
         jogador3+=1
    elif(rodada['jogador3'] < rodada['jogador4'] > rodada['jogador2']) and rodada['jogador4'] > rodada['jogador1']:
         jogador4+=1
    sortedResult = sorted(rodada.items(), key=operator.itemgetter(1), reverse=True)
    placar.append(sortedResult)
if (jogador2 < jogador1 > jogador3) and jogador1 > jogador4: # Estrutura condicional para demonstrar quem ganhou mais rodadas
    print(f'O CAMPEÃO É O JOGADOR 1 COM {jogador1} VITÓRIAS.')
elif (jogador3 < jogador2 > jogador1) and jogador2 > jogador4: 
    print(f'O CAMPEÃO É O JOGADOR 2 COM {jogador2} VITÓRIAS.')
elif (jogador2 < jogador3 > jogador1) and jogador3 > jogador4:
    print(f'O CAMPEÃO É O JOGADOR 3 COM {jogador3} VITÓRIAS.')
elif (jogador2 < jogador4 > jogador1) and jogador4 > jogador1:
    print(f'O CAMPEÃO É O JOGADOR 4 COM {jogador4} VITÓRIAS.')
else:
    print(f'Empate!! Não houveram Campeões na Partida')
print(f'=====PLACAR FINAL=====')
log = input(f'Deseja verificar o histórico de jogadas? [S/N] ').upper().strip()[0] # Exbibição da lista com todas as rodadas
if log == 'S':
    print(f'Jogadas para conferência: {placar}')
    
print('''     
             
 Obrigado🎲🎲🎲🎲🎲 Jogar!
      🎲🎲🎲Por🎲🎲🎲🎲
''')
