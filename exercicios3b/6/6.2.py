import random
def adivinha():
    numero_secreto = random.randint(1, 10)

    while True:
        n = int(input())

        if n < numero_secreto:
            print("maior")
        elif n > numero_secreto:
            print("menor")
        else:
            print("o numero secreto era", numero_secreto)
            break

adivinha()