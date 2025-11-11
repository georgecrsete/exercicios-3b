# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V8.4



def escrever_arquivo():
    with open('nomeecpf.txt', "w") as arquivo:
        for i in range(5):
            nome = input("Qual seu nome: ")
            cpf = input("qual seu cpf: ")
            arquivo.write(nome +";"+ cpf + "\n")

def ler_arquivo():
    with open('nomeecpf.txt', "r") as arquivo:
        linhas = arquivo.readlines()
        arquivo.close()

        for linha in linhas:
            print(linha.strip())


escrever_arquivo()
ler_arquivo()
