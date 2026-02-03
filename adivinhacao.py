import random

def jogar():


    numero_secreto = sortear_numero()

    rodada = 1
    pontos = 1000

    exibir_welcome()

    total_tentativas = definir_dificuldade()

    rodada, pontos = verificar_acerto(total_tentativas, numero_secreto, pontos)

    resultado = verificar_resultado(rodada, total_tentativas, numero_secreto, pontos)
    print(resultado)

    jogar_novamente()






def exibir_welcome():
    mensagem = 'Bem vindo ao jogo da Adivinhação!'
    linha = '*' * len(mensagem)
    print(linha)
    print(mensagem)
    print(linha)



def sortear_numero():
    numero_secreto = 50
    if numero_secreto is 50:
        numero_secreto = random.randrange(1, 101)
    if numero_secreto is not 50:
        return numero_secreto
    else:
        sortear_numero()



# def sortear_numero():
#     numero_secreto = random.randrange(1, 101)
#     if numero_secreto is 50:
#         sortear_numero()
#     else:
#         return numero_secreto



def pedir_numero():
    numero = input('Digite um número entre 1 a 100: ')
    return int(numero.strip())



def definir_dificuldade():
    print('\n(1)Fácil | (2)Médio | (3)Difícil')
    dificuldade = input('\nDigite a dificuldade desejada: ')
    if dificuldade == '1':
        total_tentativas = 15
    elif dificuldade == '2':
        total_tentativas = 10
    elif dificuldade == '3':
        total_tentativas = 5
    else:
        print('Opção inválida!')
    return total_tentativas



def verificar_acerto(total_tentativas, numero_secreto, pontos):
    for rodada in range(1, total_tentativas + 1):
        print(f'\nRodada {rodada} de {total_tentativas}')
        numero = pedir_numero()
        if numero == numero_secreto:
            break
        else:
            if numero > numero_secreto:
                print('Errou! dica: O número secreto é menor')
            elif numero < numero_secreto:
                print('Errou! dica: O número secreto é maior')
            pontos = calcular_pontos(numero, numero_secreto, pontos)
    return rodada, pontos



def calcular_pontos(numero, numero_secreto, pontos):
    pontos_perdidos = (abs(numero - numero_secreto))
    return pontos - pontos_perdidos



def verificar_resultado(rodada, total_tentativas, numero_secreto, pontos):
    if rodada == total_tentativas:
        return(f'\nVoce perdeu! O número secreta era {numero_secreto}\nSua pontuação: {pontos}')
    else:
        return(f'\nParabéns, você ganhou! O número secreto era {numero_secreto}\nSua pontuação: {pontos}')
    


def jogar_novamente():
    resposta = input('\nDigite 1 para jogar novamente ou 2 para voltar ao menu: ')
    if resposta == '1':
        print('\nReiniciando')
        jogar()
    elif resposta == '2':
        print('\nSaindo...')
    else:
        print('\nOpção inválida')
        jogar_novamente()



if __name__ == '__main__':
    jogar()