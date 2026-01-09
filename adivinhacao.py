import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Escolha o nivel de dificuldade: ")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Rodada {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print ("Voce digitou ", chute_str)
        chute = int(chute_str)
        
        if(chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou! Sua pontuação: {}".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! O chute foi maior que o número secreto.")
            elif(menor):
                print("Voce errou! O chute foi menor que o número secreto.")
            pontos_perdidos = round(abs(chute - numero_secreto) / 3)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")
    if(rodada == total_tentativas):
        print("O número secreto era {}, voce fez {} pontos".format(numero_secreto, pontos))

if(__name__ == "__main__"):
    jogar()