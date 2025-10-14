# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V6.3


#begin_inputs

#end_inputs

def inverter_numero():
    n = int(input("Informe um número inteiro: "))
    numero_invertido = int(str(n)[::-1])
    print("O número invertido é:", numero_invertido)

inverter_numero()