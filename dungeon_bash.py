
from personagem import Personagem
from tipo_personagem import TipoPersonagem
from mapa import Mapa

QTD_INIMIGOS_INICIAIS = 3


print("=========================")
print("Bem vindo ao Dungeon Bash!")
print("=========================")

arena = Mapa()
arena.jogador.CriarJogador()
arena.jogador.ExibirDadosDoJogador()

usr_input = input("Pressione ENTER para começar")

level = 1

while usr_input != "0":
    qtdInimigos = QTD_INIMIGOS_INICIAIS + (QTD_INIMIGOS_INICIAIS % level)
    qtdInimigos = qtdInimigos + 2 if qtdInimigos == level else qtdInimigos
    arena.GerarInimigos(qtdInimigos, level)
    arena.ExibirDadosDosInimigos()
    arena.Batalhar()
    if not arena.jogador.ativo:
        break
    level += 1
    arena.jogador.AumentarLevel(level)
    usr_input = input("Continuar para o level %s?\nPerssione ENTER para confirmar, para sair digite 0: " %level)
pass

