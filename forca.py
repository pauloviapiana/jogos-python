import random

def jogar():

    exibir_welcome()

    jogando = True
    while jogando:

        palavra_secreta = sortear_palavra() 
        casas_palavra = carregar_casas_palavra(palavra_secreta)
        print(casas_palavra)
        print('\ndica: É uma fruta')


        enforcou = False
        ganhou = False
        erros = 0

        while not enforcou and not ganhou:

            chute = pedir_letra()

            if chute in palavra_secreta:
                letra_acertada = carregar_letra_acertada(palavra_secreta, chute, casas_palavra)
                print('\n',letra_acertada)
            else:
                erros += 1
                exibir_desenho_forca(erros)
                dar_dicas(palavra_secreta, erros)

            ganhou = not '_' in letra_acertada
            enforcou = erros == 7

        if ganhou:
            exibir_mensagem_vencedor()
        elif enforcou:
            exibir_mensagem_perdedor(palavra_secreta)

        jogando = False


    jogar_novamente()


def exibir_welcome():
    mensagem = 'Bem vindo ao jogo da Forca!'
    linha = '*' * len(mensagem)
    print(linha)
    print(mensagem)
    print(linha, '\n')



def sortear_palavra():
    arquivo = open('jogos/palavras.txt', 'r')
    palavras = []

    for palavra in arquivo:
        palavra = palavra.strip()
        palavras.append(palavra)
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def carregar_casas_palavra(palavra_secreta):
   return['_' for palavra in palavra_secreta]
    

def pedir_letra():
    letra = input('\nDigite uma letra: ')
    return letra.strip().upper()

def carregar_letra_acertada(palavra_secreta, chute, casas_palavra):
    index = 0

    for letra in palavra_secreta:
        if chute == letra:
            casas_palavra[index] = chute
        index += 1
    return casas_palavra

def jogar_novamente():
        resposta = input('\nDigite 1 para jogar novamente ou 2 para voltar ao menu: ')
        if resposta == '1':
            print('\nReiniciando... ')
            jogar()
        elif resposta == '2':
            print('\nSaindo...')
        else:
            print('\nOpção inálida')
            jogar_novamente()

def exibir_desenho_forca(erros):
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

def exibir_mensagem_vencedor():
    print("\nParabéns, você ganhou!")
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

def exibir_mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
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
            

def dar_dicas(palavra_secreta, erros):
    if (palavra_secreta == 'BANANA') and (erros == 2):
        print('\ndica: É uma fruta amarela')
    elif (palavra_secreta == 'BANANA') and (erros == 5):
        print('\ndica: Os macacos gostam')
    


if __name__ == '__main__':
    jogar()