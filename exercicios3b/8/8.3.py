def ler_arquivo():
    with open("frase.txt",'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def copia_arquivo():
    conteudo = ler_arquivo()
    with open("frasecopia.txt",'w') as copiaarquivo:
        copiaarquivo.write(conteudo)
ler_arquivo()
copia_arquivo()