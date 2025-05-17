from random import randint
numRan = randint(1, 100)
tentativa = 0
while True:
    numDig = int(input('Digite um número aleatório entre 1 e 100: '))
    if not numDig == numRan:
        tentativa += 1
        print('Tente outra vez!')
        if numRan < numDig:
            print('Mire um pouco mais abaixo!')
        else:
            print('Mire um pouco mais acima!')
            if tentativa < 7:
                continue
            else:
                print('Seu número de tentativas esgotou. O número é {}, GAME OVER!' .format(numRan))
            break    
    else:
        print('Parabéns, você acertou!\nNúmero = {}' .format(numRan))
        break
        