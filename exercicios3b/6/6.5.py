# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V6.5
import random

def adivinha():
    numero_secreto = random.randint(1, 100)

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