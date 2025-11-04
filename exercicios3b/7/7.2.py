# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V7.2


#begin_inputs
letras = input().split()
palavra = input()

#end_inputs
  
def adivinha(letras, palavra):
    for i in palavra:
        if i not in letras:
            return False
        
    return True

resultado = adivinha(letras, palavra)

print(resultado)