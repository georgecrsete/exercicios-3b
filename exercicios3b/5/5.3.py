# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V5.3


cidade_taipu = 12000
taxa_taipu = 10/100 * cidade_taipu
cidade_ceara = 73000
taxa_ceara = 3/100 * cidade_ceara
cidade_parnamirim = 250000
taxa_parnamirim = 1/100 * cidade_parnamirim

#end_inputs
ano = 0

while cidade_parnamirim > cidade_ceara and cidade_parnamirim > cidade_taipu:
    cidade_taipu = cidade_taipu + taxa_taipu
    taxa_taipu = 10/100 * cidade_taipu
    cidade_ceara = cidade_ceara + taxa_ceara
    taxa_ceara = 3/100 * cidade_ceara
    cidade_parnamirim = cidade_parnamirim + taxa_parnamirim
    taxa_parnamirim = 1/100 * cidade_parnamirim
    ano += 1

print("parnamirim deixara de ser maior em {} anos.".format(ano))
