# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V6.4


#begin_inputs

#end_inputs
def craps():
    jogadas = []

    
    while True:
        try:
            jogadas.append(int(input()))
        except:
            break 

    if not jogadas:
        return

    primeira = jogadas[0]

  
    if primeira in [7, 11]:
        print("Voce ganhou!")
        return
    elif primeira in [2, 3, 12]:
        print("Voce perdeu!")
        return
    else:
        ponto = primeira
        for valor in jogadas[1:]:
            if valor == ponto:
                print("Voce ganhou!")
                return
            elif valor == 7:
                print("Voce perdeu!")
                return
       
        print("Voce perdeu!")
craps()

