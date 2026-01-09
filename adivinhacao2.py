import random
import jogos2

def jogar():

    total_tentativas = 0
    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print('*********************************')
    print('Bem vindo ao jogo da Adivinhação!')
    print('*********************************')

    print('Escolha o nível da dificuldade:')
    print('(1) Fácil \n(2) Médio \n(3) Díficil: ')

    dificuldade_escolhida = int(input('Digite a dificuldade: '))
    while(dificuldade_escolhida != 1 and dificuldade_escolhida != 2 and dificuldade_escolhida != 3):
        print('Escolha uma dificuldade 1, 2 ou 3')
        dificuldade_escolhida = int(input('Digite a dificuldade: '))

    if(dificuldade_escolhida == 1):
            total_tentativas = 20
    elif(dificuldade_escolhida == 2):
            total_tentativas = 10
    elif(dificuldade_escolhida == 3):
            total_tentativas = 5

    print('Vamos começar!')

    for rodada in range(1, total_tentativas + 1):
        print(f'Rodada: {rodada} de {total_tentativas}')
        chute = int(input('Tente adivinhar o número secreto entre 1 a 100: '))

        if(chute > 100):
            print('O número deve ser entre 1 a 100')
        elif(chute < 0):
            print('O número deve ser entre 1 a 100')

        if(chute > numero_secreto):
            print('O número secreto é menor que o chute dado')
            pontos = pontos - (abs(numero_secreto - chute) * 2)
        elif(chute < numero_secreto):
            print('O número secreto é maior que o chute dado')
            pontos = pontos - (abs(numero_secreto - chute) * 2)
        elif(chute == numero_secreto):
            print(f'Parabéns! Você ganhou!\nO número secreto era {numero_secreto}\nPontos: {pontos}')
            break
        rodada += 1

    if(rodada == total_tentativas + 1):
        print(f'Você perdeu! As chances acabaram.\nO número secreto era {numero_secreto}\nPontuação: {pontos}')

    print('Fim de jogo!')

def voltar_menu():
    voltar = (input('Digite 1 para jogar novamente ou 2 para voltar ao menu: '))
    if(voltar == '1'):
        main()
    elif(voltar == '2'):
        jogos2.iniciar_menu()
    else:
         print('Opção inválida!')
         voltar_menu()

def main():
    jogar()
    voltar_menu()

main()

if(__name__ == '__main__'):
    main()