import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_palavras_secretas(palavra_secreta) 
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    #enquanto(True)
    while(not enforcou and not acertou):

        chute = pedir_chute()

        if(chute in palavra_secreta):    
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)

        else:
            erros += 1     
            desenha_forca(erros)

        enforcou = erros == 7   
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if (acertou):
        mensagem_ganhador()
    else:    
        mensagem_perdedor(palavra_secreta)
        

        ##reiniciar = input("Tentar novamente? (Y) (N)  ").upper()
        ##if(reiniciar == "Y".upper()):
            ##return()



def imprime_mensagem_abertura():
     print("*********************************")
     print("***Bem vindo ao jogo da Forca!***")
     print("*********************************")

def carrega_palavra_secreta():
     arquivo = open("palavras.txt", "r")
     palavras = []

     for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

     arquivo.close()

     print(palavras)

     numero_aleatorio = random.randrange(0, len(palavras))
    
     palavra_secreta = palavras[numero_aleatorio].upper()
     return palavra_secreta

def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas [index] = letra        
        index += 1  

def inicializa_palavras_secretas(palavra):
    return ["_" for letra in palavra]

def pedir_chute():
    chute = input("Qual letra?  ")
    chute = chute.strip().upper()
    return chute

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_ganhador():
    print("Você GANHOU!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(palavra_secreta):
    print("Fim do jogo!")
    print("A Palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if(__name__ == "__main__"):
    jogar()
