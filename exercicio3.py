"""
    Crie uma aplicação para:
        a) Sortear um número de 0 a 1000.
            import random;
            randint(0, 1000)
        b) Faça um laço de repetição que solicite ao usuário um palpite do número.
        c) Se ele errar, informar se o palpite é MAIOR ou MENOR do que o número sorteado.
        d) Pedir novos palpites até que o usuário acerte e, depois disso, mostrar em quantas tentativas ele acertou.
"""
import random, os
os.system('cls')
print('-------> Bem vindo ao jogo de acertar o numero <-------')
SORT_NUMBER = random.randint(0, 1000)
print('>> Um numero entre 0 e 1000 foi sorteado, será que você é capaz de acerta-lo?\n')

already_tried = []
trieds = 0

jogar = True
while jogar:
    guess_number = input('Digite o seu palpite ou "stop" para desistir: ')

    if len(guess_number) == 0:
        continue
    
    if guess_number == 'stop':
        jogar = False
        continue
    
    trieds += 1
        
    if guess_number in already_tried:
        print('Este numero já foi utilizado! Vamos tentar novamente.\n')
        continue

    already_tried.append(guess_number)

    if SORT_NUMBER == int(guess_number): 
        print('\n-------> PARABÉNS! Você acertou o numero sorteado <-------')
        break
    else:
        print('Você errou!')
        if int(guess_number) > SORT_NUMBER:
            print(f'O numero {guess_number} é maior do que o numero sorteado')
        elif int(guess_number) < SORT_NUMBER:
            print(f'O numero {guess_number} é menor do que o numero sorteado')
if guess_number == 'stop':
    print('-------> Game Over <-------')
else:
    print(f'\nNumero sorteado: {SORT_NUMBER}.', f'Palpite do usuario: {guess_number}.', f'Numero de tentativas: {trieds}.', sep="\n")
