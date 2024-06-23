from database.database import read_consultas, delete_consulta
from funcionalidades.cadastroPaciente import cadastrarPaciente, get_paciente_by_telefone
from funcionalidades.cadastroConsulta import cadastrarConsulta
from datetime import datetime

    
# def cancelar_consulta():

#     todas_consultas = read_consultas()

#     if len(todas_consultas) == 0: 
#         print("Nenhum agendamento encontrado")
#         return 

#     for i, consulta in enumerate(todas_consultas): 
#         paciente = get_paciente_by_telefone(consulta["telefone"])
#         print(f"{i + 1} - paciente {paciente['nome']} com consulta agendada para o dia {consulta['data']} às {consulta['hora']} para especialista em {consulta['especialidade']}")

#     numero_agendamento = int(input("Selecione uma consulta: "))

#     nome_paciente =  get_paciente_by_telefone(todas_consultas[numero_agendamento - 1]["telefone"])

#     data = todas_consultas[numero_agendamento - 1]['data']

#     horario = todas_consultas[numero_agendamento - 1]['hora']

#     especialidade = todas_consultas[numero_agendamento - 1]['especialidade']
    
#     print(f"Paciente:{nome_paciente['nome']}\nDia: {data}\nHora: {horario}\nEspecialidade: {especialidade}")

#     print("Deseja:\n1 - Remarcar a consulta\n2- Cancelar consulta")

#     escolha = input("Digite o número da escolha: ")

#     if escolha == "1": 
        
#     elif escolha == "2": 
#         delete_consulta(nome_paciente ['telefone'], data, horario)

def show_menu():
    while True:
        print('\nEscolha uma opção:')
        print('1. Cadastrar paciente')
        print('2. Marcar consulta')
        print('3. Cancelar/Remarcar consulta')
        print('4. Sair')
        
        choice = input('Digite o número da opção desejada: ')

        if choice == '1':
            retorno = cadastrarPaciente()
            print(retorno)
        elif choice == '2':
            # print('Você escolheu a Opção 2')
            cadastrarConsulta()
        elif choice == '3':
            # print('Você escolheu a Opção 3')
            # print(read_pacientes())
            cancelar_consulta()
        elif choice == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

show_menu()