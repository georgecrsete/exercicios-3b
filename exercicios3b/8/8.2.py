# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V8.2


def escrever_arquivo():
    with open('frase.txt', "w") as arquivo:
        for i in range(5):
            frase = input("digite uma frase: ")
            arquivo.write(frase + "\n")
def contar_arquivo():
    with open("frase.txt",'r') as arquivo:
       linhas = arquivo.readlines()
    quantidade = len(linhas)
    print(f"O arquivo tem {quantidade} linhas.")
escrever_arquivo()
contar_arquivo()