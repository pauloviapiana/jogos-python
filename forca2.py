import random


def jogar():

    jogando = True
    while jogando:

        imprimir_mensagem_abertura()
        palavra_secreta = carregar_palavra_secreta()

        letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
        print(letras_acertadas)

        acertou = False
        enforcou = False
        erros = 0

        while (not acertou and not enforcou):

            chute = pedir_chute()

            if(chute in palavra_secreta):
                marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
            else:
                erros += 1
                desenhar_forca(erros)
            
            enforcou = erros == 7
            acertou = '_' not in letras_acertadas

            print(letras_acertadas)
        
        if (acertou):
            imprimir_mensagem_vencedor()
        elif(enforcou):
            imprimir_mensagem_perdedor(palavra_secreta)

        while True:
            resposta = input('Digite 1 para jogar novamente ou 2 para voltar ao menu: ')

            if resposta == '1':
                print('Reiniciando...')
                break
            elif resposta == '2':
                print('Saindo do jogo')
                jogando = False
                break
            else:
                print('Opção inválida, digite 1 ou 2')


def imprimir_mensagem_abertura():
    print('***************************')
    print('Bem vindo ao jogo da Forca!')
    print('***************************')

def carregar_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializar_letras_acertadas(palavra):
    return['_' for letra in palavra]
    # e se colocar palavra secreta?

def pedir_chute():
    chute = input('Qual letra? ')
    chute = chute.strip().upper()
    return chute

def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprimir_mensagem_vencedor():
    print("Parabéns, você ganhou!")
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

def imprimir_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print(" /                   \  ")
    print(" |   XXXX     XXXX   |    ")
    print(" |   XXXX     XXXX   |     ")
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

if __name__ == '__main__':
    jogar()