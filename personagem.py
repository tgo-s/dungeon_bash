from tipo_personagem import TipoPersonagem
import random

VIDA_JOGADOR = 100
FORCA_JOGADOR = 10

class Personagem:
    
    def CriarJogador(self):
        self.nome = input("Entre com o nome do seu personagem: ")
        self.tipo = TipoPersonagem.JOGADOR
        self.vida = VIDA_JOGADOR
        self.totalVida = VIDA_JOGADOR
        self.forca = FORCA_JOGADOR
        self.level = 1
        self.ativo = True
    pass

    def CriarPersonagem(self, nome, tipo, vida, forca, level ):
        self.nome = nome
        self.tipo = tipo
        self.vida = vida
        self.forca = forca
        self.level = level
    pass

    def ExibirDadosDoJogador(self):
        print("Dados do jogador: ")
        print("-------------------------")
        print("Nome : %s" %self.nome)
        print("Tipo : %s" %self.tipo.name)
        print("Vida : %d" %self.vida)
        print("Força: %d" %self.forca)
        print("Level: %d" %self.level)
        print("-------------------------")
    pass

    def AumentarLevel(self, level):
        pontosVida = random.randint(5, 10)
        pontosForca = random.randint(1, 5)
        self.vida = self.totalVida
        print("\n-------------------------")
        print("%s subiu para o nivel %d" %(self.nome, level))
        print("Seus pontos de vida foram restaurados!")
        print("Vida : %d (+%d)" %(self.vida, pontosVida ))
        print("Força: %d (+%d)" %(self.forca, pontosForca ))
        print("-------------------------")
        self.vida += pontosVida
        self.totalVida = self.vida
        self.forca += pontosForca
        self.level = level

        
        