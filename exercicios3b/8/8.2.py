# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V8.2


def escrever_arquivo():
    with open('text.t', "w") as arquivo:
        frase = input("digite uma frase: ")
        for i in range(5):
            arquivo.write(frase)
def contar_arquivo():
    with open("text.t",'r') as arquivo:
       linhas = arquivo.readlines()
    quantidade = len(linhas)
    print(f"O arquivo tem {quantidade} linhas.")
escrever_arquivo()
contar_arquivo()