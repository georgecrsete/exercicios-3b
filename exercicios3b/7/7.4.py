# @cikey 67674417a027ae17ee1925a4537fb74e
# @sid 20251174010012
# @aid V7.4

lista_contato = []

def contato_novo():
    nome = input('Digite seu nome: ')
    telefone = input('Digite seu número: ')

    contato = {'nome': nome, 'telefone': telefone}
    lista_contato.append(contato)
    print('Contato adicionado com sucesso!')

def consulta_por_nome(nome_pessoa):
    for contato in lista_contato:
        if contato['nome'].lower() == nome_pessoa.lower():
            return contato['telefone']
    return "Contato não encontrado."



contato_novo()  

nome_busca = input("Digite o nome que deseja buscar: ")
print(consulta_por_nome(nome_busca))

