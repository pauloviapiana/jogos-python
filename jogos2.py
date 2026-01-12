import adivinhacao2
import forca

def iniciar_menu():
    print('***************************')
    print('Bem vindo ao menu de jogos!')
    print('***************************')

    print('(1) Adivinhação')
    print('(2) Forca')

    escolha_jogo = int(input('Digite qual jogo voce quer jogar: '))

    if(escolha_jogo == 1):
        print('Você escolheu o jogo da Adivinhação!')
        adivinhacao2.jogar()
        iniciar_menu()
    elif(escolha_jogo == 2):
        forca.jogar()
        iniciar_menu()

if(__name__ == '__main__'):
    iniciar_menu()