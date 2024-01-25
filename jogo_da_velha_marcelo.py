opcao, cont = 0 , 0, 
jogadorXvenceu, jogadorOvenceu = False, False
tabuleiro = [
    ['','',''],
    ['','',''],
    ['','',''],
]

# função para mostrar as regiões pros jogadores escolherem
def tabuleiro_para_mostrar_regioes():
    if (cont < 9) and (jogadorOvenceu == False) and (jogadorXvenceu == False): #Será executada somente se não houver vencedor
        print("\nEscolha a regiao desejada, conforme os números a seguir:\n")     
        print("| 1 | 2 | 3 |")
        print("| 4 | 5 | 6 |")
        print("| 7 | 8 | 9 |")
        print()


# função para mostrar o Tabuleiro 
def mostrar_tabuleiro():
    global tabuleiro
    print("tabuleiro atual:")
    for t in tabuleiro:
        print(" | ".join(t))
        print("----------")

# função para definir a jogada do jogador 1, preenchendo o espaço vazio      
def jogadaX():
    
    global jogadorXvenceu
    global jogadorOvenceu
    global tabuleiro
    global cont
    
    # a função só será executada se ainda não tiver vencedor no jogo
    if (jogadorXvenceu == False) and (jogadorOvenceu == False):
                    

        while True:
            
            jogadaX = int(input("\nPara o Jogador 1 - Informe a Região Desejada para preencher com 'X': "))
            
            if (jogadaX == 1) and (tabuleiro[0][0] == ''):
                tabuleiro[0][0] = "X"
                cont +=1
                return
            elif (jogadaX == 2) and (tabuleiro[0][1] == ''):
                tabuleiro[0][1] = "X"
                cont +=1
                return
            elif (jogadaX == 3) and (tabuleiro[0][2] == ''):
                tabuleiro[0][2] = "X"
                cont +=1
                return
            elif (jogadaX == 4) and (tabuleiro[1][0] == ''):
                tabuleiro[1][0] = "X"
                cont +=1
                return      
            elif (jogadaX == 5) and (tabuleiro[1][1] == ''):
                tabuleiro[1][1] = "X"
                cont +=1
                return
            elif (jogadaX == 6) and (tabuleiro[1][2] == ''):
                tabuleiro[1][2] = "X"
                cont +=1
                return
            elif (jogadaX == 7) and (tabuleiro[2][0] == ''):
                tabuleiro[2][0] = "X"
                cont +=1
                return
            elif (jogadaX == 8) and (tabuleiro[2][1] == ''):
                tabuleiro[2][1] = "X"
                cont +=1
                return
            elif (jogadaX == 9) and (tabuleiro[2][2] == ''):
                tabuleiro[2][2] = "X"
                cont +=1
                return
            else:
                print("\nRegião inválida! Escolha outra opção!\n")
    else:
        return
        
    
                
# função para definir a jogada do jogador 2, preenchendo o espaço vazio      
def jogadaO():
    
    global jogadorXvenceu
    global jogadorOvenceu
    global tabuleiro
    global cont
        
    # a função só será executada se ainda não tiver vencedor no jogo
    if (jogadorXvenceu == False) and (jogadorOvenceu == False):
                    

        while True:
            
            jogadaO = int(input("\nPara o Jogador 2 - Informe a Região Desejada para preencher com 'O': "))
            
            if (jogadaO == 1) and (tabuleiro[0][0] == ''):
                tabuleiro[0][0] = "O"
                cont +=1
                return
            elif (jogadaO == 2) and (tabuleiro[0][1] == ''):
                tabuleiro[0][1] = "O"
                cont +=1
                return
            elif (jogadaO == 3) and (tabuleiro[0][2] == ''):
                tabuleiro[0][2] = "O"
                cont +=1
                return
            elif (jogadaO == 4) and (tabuleiro[1][0] == ''):
                tabuleiro[1][0] = "O"
                cont +=1
                return      
            elif (jogadaO == 5) and (tabuleiro[1][1] == ''):
                tabuleiro[1][1] = "O"
                cont +=1
                return
            elif (jogadaO == 6) and (tabuleiro[1][2] == ''):
                tabuleiro[1][2] = "O"
                cont +=1
                return
            elif (jogadaO == 7) and (tabuleiro[2][0] == ''):
                tabuleiro[2][0] = "O"
                cont +=1
                return
            elif (jogadaO == 8) and (tabuleiro[2][1] == ''):
                tabuleiro[2][1] = "O"
                cont +=1
                return
            elif (jogadaO == 9) and (tabuleiro[2][2] == ''):
                tabuleiro[2][2] = "O"
                cont +=1
                return
            else:
                print("\nRegião inválida! Escolha outra opção!\n")
    else:
        return

                

        
#função para verificar se tem algum vencedor
def verificar_vencedor():
    
    global jogadorXvenceu
    global jogadorOvenceu
    global tabuleiro
    
    
    #primeira linha
    if (tabuleiro[0][0] == 'X') and (tabuleiro[0][1] == 'X') and (tabuleiro[0][2] == 'X'):
        jogadorXvenceu = True
        print("\n ||||| COMPLETADO A PRIMEIRA LINHA!! (Jogando com 'X') ||||| \n")
    elif (tabuleiro[0][0] == 'O') and (tabuleiro[0][1] == 'O') and (tabuleiro[0][2] == 'O'):
        jogadorOvenceu = True
        print("\n ||||| COMPLETADO A PRIMEIRA LINHA!! (Jogando com 'O') ||||| \n")

    #segunda linha
    elif (tabuleiro[1][0] == 'X') and (tabuleiro[1][1] == 'X') and (tabuleiro[1][2] == 'X'):
        jogadorXvenceu = True
        print("\n ||||| COMPLETADO A SEGUNDA LINHA!! (Jogando com 'X') ||||| \n")
    elif (tabuleiro[1][0] == 'O') and (tabuleiro[1][1] == 'O') and (tabuleiro[1][2] == 'O'):
        jogadorOvenceu = True
        print("\n ||||| COMPLETADO A SEGUNDA LINHA!! (Jogando com 'O') ||||| \n")
        
    #terceira linha
    elif (tabuleiro[2][0] == 'X') and (tabuleiro[2][1] == 'X') and (tabuleiro[2][2] == 'X'):
        jogadorXvenceu = True
        print("\n ||||| COMPLETADO A TERCEIRA LINHA!! (Jogando com 'X') ||||| \n")
    elif (tabuleiro[2][0] == 'O') and (tabuleiro[2][1] == 'O') and (tabuleiro[2][2] == 'O'):
        jogadorOvenceu = True
        print("\n ||||| COMPLETADO A TERCEIRA LINHA!! (Jogando com 'O') ||||| \n")
        
    #primeira coluna
    elif (tabuleiro[0][0] == 'X') and (tabuleiro[1][0] == 'X') and (tabuleiro[2][0] == 'X'):
        jogadorXvenceu = True
        print("\n ||||| COMPLETADO A PRIMEIRA COLUNA!! (Jogando com 'X') ||||| \n")
    elif (tabuleiro[0][0] == 'O') and (tabuleiro[1][0] == 'O') and (tabuleiro[2][0] == 'O'):
        jogadorOvenceu = True
        print("\n ||||| COMPLETADO A PRIMEIRA COLUNA!! (Jogando com 'O') ||||| \n")
        
    #segunda coluna
    elif (tabuleiro[0][1] == 'X') and (tabuleiro[1][1] == 'X') and (tabuleiro[2][1] == 'X'):
        jogadorXvenceu = True
        print("\n ||||| COMPLETADO A SEGUNDA COLUNA!! (Jogando com 'X') ||||| \n")
    elif (tabuleiro[0][1] == 'O') and (tabuleiro[1][1] == 'O') and (tabuleiro[2][1] == 'O'):
        jogadorOvenceu = True
        print("\n ||||| COMPLETADO A SEGUNDA COLUNA!! (Jogando com 'O') ||||| \n")
        
    #terceira coluna
    elif (tabuleiro[0][2] == 'X') and (tabuleiro[1][2] == 'X') and (tabuleiro[2][2] == 'X'):
        jogadorXvenceu = True
        print("\n ||||| COMPLETADO A TERCEIRA COLUNA!! (Jogando com 'X') ||||| \n")
    elif (tabuleiro[0][2] == 'O') and (tabuleiro[1][2] == 'O') and (tabuleiro[2][2] == 'O'):
        jogadorOvenceu = True
        print("\n ||||| COMPLETADO A TERCEIRA COLUNA!! (Jogando com 'O') ||||| \n")
        
    #primeira diagonal
    elif (tabuleiro[0][0] == 'X') and (tabuleiro[1][1] == 'X') and (tabuleiro[2][2] == 'X'):
        jogadorXvenceu = True
        print("\n ||||| COMPLETADO EM DIAGONAL!! (Jogando com 'X') ||||| \n")
    elif (tabuleiro[0][0] == 'O') and (tabuleiro[1][1] == 'O') and (tabuleiro[2][2] == 'O'):
        jogadorOvenceu = True
        print("\n ||||| COMPLETADO EM DIAGONAL!! (Jogando com 'O') ||||| \n")
    
    #segunda diagonal
    elif (tabuleiro[2][0] == 'X') and (tabuleiro[1][1] == 'X') and (tabuleiro[0][2] == 'X'):
        jogadorXvenceu = True
        print("\n ||||| COMPLETADO EM DIAGONAL!! (Jogando com 'X') ||||| \n")
    elif (tabuleiro[2][0] == 'O') and (tabuleiro[1][1] == 'O') and (tabuleiro[0][2] == 'O'):
        jogadorOvenceu = True
        print("\n ||||| COMPLETADO EM DIAGONAL!! (Jogando com 'O') ||||| \n")

# Função para zerar as variaveis, para reiniciar o jogo
def reiniciar():
    
    global jogadorXvenceu
    global jogadorOvenceu
    global tabuleiro
    global cont
    
    # Reiniciar o tabuleiro, para voltar a jogar
    tabuleiro = [
        ['','',''],
        ['','',''],
        ['','',''],
        ]
    
    # Reiniciar as variáveis, para voltar a jogar
    jogadorXvenceu = False
    jogadorOvenceu = False
    cont = 0
        
# Aqui começa o JOGO DA VELHA
while opcao != 985412587455154:
    
    # usuário deve escolher se deseja jogar ou não
    opcao = int(input("\nDeseja jogar o JOGO DA VELHA?\n \nDigite qualquer número para jogar \nDigite '985412587455154' para encerrar o jogo\n \nEscolha: "))
    
    
        
    if opcao != 985412587455154: # Caso o usuário digite qualquer número diferente de "985412587455154", será iniciado o jogo
        
        # Opção pro usuário caso deseja verificar as regras do jogo
        regras = int(input("\nDeseja verificar AS REGRAS do JOGO DA VELHA antes de iniciar?\n \nDigite qualquer número para seguir o jogo\nDigite '123' para conhecer as regras do jogo\n \nEscolha: "))

        # Impressão das regras do jogo, para conhecimento, caso seja desejo do usuário
        if regras == 123:
            print("\nRegras do Jogo da Velha: \n")
            print("\n1 - Grade de Jogo: O jogo é disputado em uma grade 3x3, formando um total de 9 espaços para preencher.\n")
            print("\n2 - Jogadores: São necessários dois jogadores, cada um representado por um símbolo, geralmente 'X' e 'O'.\n")
            print("\n3 - Alternância de Turnos: Os jogadores alternam seus turnos para colocar seus símbolos na grade, um por vez.\n")
            print("\n4 - Objetivo: O objetivo é formar uma linha horizontal, vertical ou diagonal com três símbolos iguais (X ou O).\n")
            print("\n5 - Vitória: Se um jogador conseguir alinhar três dos seus símbolos de forma consecutiva (horizontal, vertical ou diagonal), ele vence a partida.\n")
            print("\n6 - Empate: Se todos os espaços forem preenchidos e nenhum jogador conseguir formar uma linha de três símbolos iguais, o jogo termina em empate.\n")
            
        reiniciar()    
        print("\n****** Orientações pro Jogo ******\n")
        print("O primeiro jogador utilizará o valor 'X'")
        print("\nO segundo jogador utilizará o valor 'O'")
        print("\nCaso seja escolhida uma opção diferente das regiões disponíveis, ou uma região que já foi preenchida, será informado para escolher outra região\n")

        while (cont < 9):
                            
            tabuleiro_para_mostrar_regioes() # Mostra as opções de regiões pra orientar os jogadores
            mostrar_tabuleiro() # Tabuleiro com as jogadas efetuadas
            jogadaX() # função para preencher as regiões escolhidas pelo jogador 1
            verificar_vencedor() # Verifica se há vencedor no jogo, após o jogador 1 fazer a jogada dele
            
            if (jogadorXvenceu == True):
                break # Encerra o loop se o jogador 1 vencer
            
            if (cont == 9):
                break # Encerra o loop se completou as 9 jogadas possíveis
            
            tabuleiro_para_mostrar_regioes() # Mostra as opções de regiões pra orientar os jogadores
            mostrar_tabuleiro() # Tabuleiro com as jogadas efetuadas
            jogadaO() # função para preencher as regiões escolhidas pelo jogador 2
            verificar_vencedor() # Verifica se há vencedor no jogo, após o jogador 1 fazer a jogada dele
            
            if (jogadorOvenceu == True):
                break # Encerra o loop se o jogador 2 vencer
            
            if (cont == 9):
                break # Encerra o loop se completou as 9 jogadas possíveis
            
            
                        
        if (jogadorXvenceu == True): # Caso o jogador 1 ganhe o jogo, sendo dado parabéns ao mesmo
            
            mostrar_tabuleiro() # Tabuleiro com as jogadas efetuadas
            print("\n ||||| O JOGADOR 1 VENCEU --- PARABÉNS!! ||||| \n")
        
        
        elif (jogadorOvenceu == True): # Caso o jogador 2 ganhe o jogo, sendo dado parabéns ao mesmo
            
            mostrar_tabuleiro() # Tabuleiro com as jogadas efetuadas
            print("\n ||||| O JOGADOR 2 VENCEU --- PARABÉNS!! ||||| \n")
        
        else: # condição caso os jogadores tenham feito 9 jogadas e não houver vencedor
            
            mostrar_tabuleiro() # Tabuleiro com as jogadas efetuadas
            print("\n ||||| TODAS AS REGIÕES FORAM PREENCHIDAS, NÃO HOUVE GANHADOR! ||||| \n")
            

                
    else:
        print("Jogo Encerrado!") # Caso o usuário digite "985412587455154" no inicio, encerrando o jogo...
        break
                    
