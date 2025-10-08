# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V6.2


#begin_inputs

#end_inputs



n = int(input("diga numero"))
def faça_numeros(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
faça_numeros(n)