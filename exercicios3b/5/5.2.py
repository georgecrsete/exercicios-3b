# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V5.2

#begin_inputs

#end_inputs

minutos = 0   

pos_tartaruga = 500
pos_lebre = 0

vel_tartaruga = 1
vel_lebre = 10

while pos_lebre < pos_tartaruga:
    minutos += 1
    pos_tartaruga += vel_tartaruga
    pos_lebre += vel_lebre

print(minutos)

