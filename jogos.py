import forca
import adivinhacao

def escolhe_jogo():
    print("**************Ei!****************")
    print("*******Escolha o jogo!***********")
    print("**Vamos ver se você é Bom mesmo**")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
