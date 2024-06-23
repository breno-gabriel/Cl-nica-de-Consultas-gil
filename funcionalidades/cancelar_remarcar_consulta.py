from database.database import read_consultas, delete_consulta, update_consulta
from funcionalidades.cadastroPaciente import cadastrarPaciente, get_paciente_by_telefone
from utils.funcoes_uteis import selecao_especialidade,selecao_data, selecao_horario

def cancelar_consulta():

    todas_consultas = read_consultas()

    if len(todas_consultas) == 0: 
        print("Nenhum agendamento encontrado")
        return 

    for i, consulta in enumerate(todas_consultas): 
        paciente = get_paciente_by_telefone(consulta["telefone"])
        print(f"{i + 1} - paciente {paciente['nome']} com consulta agendada para o dia {consulta['data']} às {consulta['hora']} para especialista em {consulta['especialidade']}")

    numero_agendamento = int(input("Selecione uma consulta: "))

    nome_paciente =  get_paciente_by_telefone(todas_consultas[numero_agendamento - 1]["telefone"])

    data = todas_consultas[numero_agendamento - 1]['data']

    horario = todas_consultas[numero_agendamento - 1]['hora']

    especialidade = todas_consultas[numero_agendamento - 1]['especialidade']
    
    print(f"Paciente:{nome_paciente['nome']}\nDia: {data}\nHora: {horario}\nEspecialidade: {especialidade}")

    print("Deseja:\n1 - Remarcar a consulta\n2- Cancelar consulta")

    escolha = input("Digite o número da escolha: ")

    if escolha == "1": 
        #Recebendo e validando a data da consulta.
        dia = selecao_data()

        #Recebendo e e validando o horário da consulta.
        hora = selecao_horario(data)

        # Recebendo e validando escolha da especialidade.
        especialidade_escolhida = selecao_especialidade()

        consulta = {
            'data': data,
            'hora': f"{int(hora) + 7}:00",
            'especialidade': especialidade_escolhida
        }

        #Atualizando o registro. 
        update_consulta(nome_paciente ['telefone'], data, horario, consulta)

    elif escolha == "2": 
        delete_consulta(nome_paciente ['telefone'], data, horario)