banco_dados_paciente = []

def verificar_existência(bd, telefone): 
    
    for cadastro in bd:
        if cadastro["telefone"] == telefone:
            return True 
        else:
            return False 


def cadastrar(nome, telefone): 

    if verificar_existência(banco_dados_paciente, telefone):
        return "Paciente já cadastrado!"
    else: 

        paciente = {
        "nome": nome, 
        "telefone": telefone
        }

        banco_dados_paciente.append(paciente)
        return "Paciente cadastrado com sucesso"

def show_menu():
    while True:
        print('\nEscolha uma opção:')
        print('1. Cadastrar')
        print('2. Opção 2')
        print('3. Opção 3')
        print('4. Sair')
        
        choice = input('Digite o número da opção desejada: ')

        if choice == '1':
            nome = input("Digite o nome do paciente: ")
            telefone = input("Digite o telefone do paciente: ")
            mensagem = cadastrar(nome, telefone)
            print(mensagem)
        elif choice == '2':
            print('Você escolheu a Opção 2')
        elif choice == '3':
            print('Você escolheu a Opção 3')
        elif choice == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

show_menu()