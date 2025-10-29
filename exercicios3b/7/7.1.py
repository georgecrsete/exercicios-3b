# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V7.1


from string import ascii_lowercase

def letras_disponiveis(letras):
    
    alfabeto = set(ascii_lowercase)
    letras_usadas = set(letras)
    
    
    return sorted(alfabeto - letras_usadas)


#begin_inputs
letras = ['a', 'e', 'i', 'o', 'u']
#end_inputs


print(letras_disponiveis(letras))
