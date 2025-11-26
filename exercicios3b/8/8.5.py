# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V8.5

def adicionar_contato(contatos):
    tel = input("telefone: ")
    nome = input("Nome: ")
    contatos[tel] = nome
    print("Contato adicionado com sucesso!\n")

def salvar_cont(contatos):
    with open("contatos2.txt", "w") as arquivo:
        for tel, nome in contatos.items():
            arquivo.write(f"{nome};{tel}\n")
    print("Contatos salvos no arquivo!\n")

def mostrar_contatos():
    contatos = {}
    try:
        with open("contatos2.txt", "r") as arquivo:
            for linha in arquivo:
                tel, nome = linha.strip().split(";")
                contatos[tel] = nome
        print("Contatos carregados do arquivo!\n")
    except FileNotFoundError:
        print("Arquivo ainda nao existe.\n")
    return contatos

def remover_contato(contatos):
    nome = input("Digite o NOME do contato que deseja remover: ")
    if nome in contatos:
        del contatos[nome]
        print("Contato removido com sucesso!\n")
    else:
        print("NOME não encontrado/n")
    
def main():
    contatos = mostrar_contatos()
    while True:
        print("        ")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Mostrar contatos")
        print("4 - Salvar contatos")
        print("5 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            adicionar_contato(contatos)
        elif opcao == "2":
            remover_contato(contatos)
        elif opcao == "3":
            for tel, nome in contatos.items():
                print(f"{tel} - {nome}")
            print()
        elif opcao == "4":
            salvar_cont(contatos)
        elif opcao == "5":
                salvar_cont(contatos)
                print("Encerrando...")
                break
        else:
            print("Opcao invalida!\n")
main()