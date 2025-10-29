import random

def adivinha2():
    numADV = random.randint(1, 1000)
    trys = 0
    while True:
        palpite = int(input("Digite um numero entre 1 e 1000: "))
        trys += 1
        if trys >= 10:
            print("acabou suas chances")
            break

        if palpite < numADV:
            print("O numero secreto e maior.")
        elif palpite > numADV:
            print("O numero secreto e menor.")
        else:
            print(f"Parabens! Você acertou! O numero secreto era {numADV}.")
            break
       
adivinha2()