# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V8.1
def escrever_arquivo():
    with open('text.txt', "w") as arquivo:
        frase = input("digite uma frase: ")
        arquivo.write(frase)
def ler_arquivo():
    with open("text.txt",'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:", conteudo)

escrever_arquivo()
ler_arquivo()