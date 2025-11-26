# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V8.3



def ler_arquivo():
    with open("frase83.txt",'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def copia_arquivo():
    conteudo = ler_arquivo()
    with open("frasecopia83.txt",'w') as copiaarquivo:
        copiaarquivo.write(conteudo)
ler_arquivo()
copia_arquivo()