import os
import adivinhacao, forca

def menu():
    
    os.system('clear')
    exibir_welcome()
    exibir_options()




def exibir_welcome():
    mensagem = 'Bem vindo ao menu de jogos Python!'
    linha = '*' * len(mensagem)
    print(linha)
    print(mensagem)
    print(linha)

def exibir_options():
    print('\n(1)Adivinhação | (2)Forca')
    option = input('\nDigite qual jogo voce deseja jogar: ')
    if option == '1':
        os.system('clear')
        adivinhacao.jogar()
        menu()
    elif option == '2':
        os.system('clear')
        forca.jogar()
        menu()
    else:
        os.system('clear')
        print('Opção inválida!')
        exibir_options()

if __name__ == '__main__':
    menu()
    