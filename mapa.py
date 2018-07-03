from personagem import Personagem
from tipo_personagem import TipoPersonagem
from random import randint
import math

INTENSIFICADOR_LEVEL_BOSS = 3

class Mapa:
    
    def __init__(self):
        self.jogador = Personagem()
        self.inimigos = []

    def GerarInimigos(self, qtdInimigos, level):
        print("\nGerando inimigos...")
        self.inimigos = []
        for n in range(qtdInimigos):
            if (n+1) == qtdInimigos:
                levelBoss =  level + INTENSIFICADOR_LEVEL_BOSS if level > 1 else INTENSIFICADOR_LEVEL_BOSS
                vidaBoss = randint(20,40)
                forcaBoss = randint(20,25)

                if level > 1:
                    vidaBoss = math.ceil(vidaBoss + levelBoss + (vidaBoss*0.1))
                    forcaBoss = math.ceil(forcaBoss + levelBoss + (forcaBoss*0.1))
                pass

                p = Personagem()
                p.CriarPersonagem("Synister Lord of the Beasts", TipoPersonagem.BOSS, vidaBoss, forcaBoss, levelBoss)    
                self.inimigos.append(p)
            else:
                levelMonstro = randint(level-2 if (level-2) > 0 else 1, level+1) if level > 1 else level
                vidaMonstro = randint(10,25)
                forcaMonstro = randint(5,10)

                if level > 1:
                    vidaMonstro = math.ceil(vidaMonstro + levelMonstro + (vidaMonstro*0.1))
                    forcaMonstro = math.ceil(forcaMonstro + levelMonstro + (forcaMonstro*0.1))
                pass

                p = Personagem()
                p.CriarPersonagem("Synister Beast", TipoPersonagem.MONSTRO, vidaMonstro, forcaMonstro, levelMonstro)
                self.inimigos.append(p)
                 
                
        # print("Inimigos[%d]" %len(self.inimigos))
        
    

    def ExibirDadosDosInimigos(self):
        print("Inimigos criados")
        print("-------------------------")
        for inimigo in self.inimigos:
            print("Nome : %s" %inimigo.nome)
            print("Tipo : %s" %inimigo.tipo.name)
            print("Vida : %d" %inimigo.vida)
            print("Força: %d" %inimigo.forca)
        pass
        print("-------------------------")
    pass

    def Batalhar(self):
        for inimigo in self.inimigos:
            print("-------------------------")
            print("%s encontrou um %s!" %(self.jogador.nome, inimigo.nome) )
            usr_input = input("\nAtacar (a), Defender (d), Fugir (f) ? ")

            while usr_input != "f":
                if usr_input == "a":
                    
                    if inimigo.vida <= 0:
                        break
                    
                    print("\n%s(%d) atacou o inimigo %s(%d)" %(self.jogador.nome, self.jogador.vida, inimigo.nome, inimigo.vida))
                    inimigo.vida -= self.jogador.forca
                    print("%s recebeu -%d de dano" %(inimigo.nome, self.jogador.forca))
                    
                    if inimigo.vida <= 0:
                        print("O inimigo %s foi derrotado!" %inimigo.nome)
                        break 
                    pass

                    print("%s(%d) atacou %s(%d)" %(inimigo.nome, inimigo.vida, self.jogador.nome, self.jogador.vida))
                    self.jogador.vida -= inimigo.forca
                    print("%s(%d) recebeu -%d de dano" %(self.jogador.nome, self.jogador.vida, inimigo.forca))

                    if self.jogador.vida <= 0:
                        print("%s foi derrotado! " %self.jogador.nome)
                        self.jogador.ativo = False
                        print("***********************")
                        print("\tGAME OVER!")
                        print("***********************")
                        break
                elif usr_input == "d":
                    print("%s(%d) usou a defesa" %(self.jogador.nome, self.jogador.vida))
                    print("%s(%d) atacou %s(%d)" %(inimigo.nome, inimigo.vida, self.jogador.nome, self.jogador.vida))
                    danoDefendido = (inimigo.forca - (self.jogador.forca / 2))
                    self.jogador.vida -= danoDefendido
                    print("%s recebeu -%d de dano" %(self.jogador.nome, danoDefendido))

                    if self.jogador.vida <= 0:
                        print("%s foi derrotado! " %self.jogador.nome)
                        self.jogador.ativo = False
                        print("**********************!")
                        print("\tGAME OVER!")
                        print("**********************!")
                        break
                pass
                

                usr_input = input("\nAtacar (a), Defender (d), Fugir (f) ? ")
            pass

            if usr_input == "f":
                usr_input = input("Deseja mesmo abandonar o jogo? (s/n)")
                if usr_input == "s":
                    print("%s amarelou e fugiu do jogo!" %self.jogador.nome)
                    print("**********************!")
                    print("\tGAME OVER!")
                    print("**********************!")
                    self.jogador.ativo = False
                    break
            
        pass
    pass

pass