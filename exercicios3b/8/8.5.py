# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V8.5


def contatos():
    with open('contatos.txt', "a") as arquivo:
        for i in range(3):
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            arquivo.write(nome +";"+ telefone + "\n")
        print("contato salvo com sucesso!")

    with open("contatos.txt", "r") as arquivo:
        print("\nContatos cadastrados:")
        for linha in arquivo:
            print(linha.strip())
contatos()