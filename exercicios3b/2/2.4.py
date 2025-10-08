# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V2.4


#begin_inputs

valor_compra = float(input("Digite o valor da compra: "))

  

#end_inputs

avista = valor_compra * 0.91
parcela5x = valor_compra / 5
parcela10x = (valor_compra * 1.17) / 10

print(round(avista, 2))
print(round(parcela5x, 2))
print(round(parcela10x, 2))