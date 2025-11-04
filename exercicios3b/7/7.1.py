# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V7.1

#begin_inputs
  
letras = input().split(' ')
  
#end_inputs
  
from string import ascii_lowercase

def letras_fornecidas(letras):
    letras_chutar = []
    for i in ascii_lowercase:
        if i not in letras:
            letras_chutar.append(i)
    return letras_chutar



disponiveis = letras_fornecidas(letras)
print(disponiveis)