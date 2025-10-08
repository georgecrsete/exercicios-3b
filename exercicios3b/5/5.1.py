# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V5.1


#begin_inputs


#end_inputs

	

def main():
    limite = 500
    soma = 0

    while True:
        peso = int(input())
        if soma + peso > limite:
            print("Peso excedido")
            break
        soma += peso

main()