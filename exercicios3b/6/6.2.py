# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V6.2


#begin_inputs
n = int(input())
#end_inputs




def faca_numeros(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
faca_numeros(n)