from database.database import read_consultas, delete_consulta, update_consulta
from funcionalidades.cadastroPaciente import cadastrarPaciente, get_paciente_by_telefone
from utils.funcoes_uteis import selecao_especialidade,selecao_data, selecao_horario, RED, GREEN, YELLOW, BLUE, RESET

def cancelar_consulta():

    todas_consultas = read_consultas()

    if len(todas_consultas) == 0: 
        print("Nenhum agendamento encontrado")
        input("Pressione Enter para continuar...")
        return 

    for i, consulta in enumerate(todas_consultas): 
        paciente = get_paciente_by_telefone(consulta["telefone"])
        print(f"{i + 1} - paciente {paciente['nome']} com consulta agendada para o dia {consulta['data']} às {consulta['hora']} para especialista em {consulta['especialidade']}")
    print(f"{len(todas_consultas) + 1} - Voltar ao menu principal")

    print()

    numero_agendamento = int(input("Selecione uma consulta: "))

    if numero_agendamento == len(todas_consultas) + 1:
        return 

    nome_paciente =  get_paciente_by_telefone(todas_consultas[numero_agendamento - 1]["telefone"])

    data = todas_consultas[numero_agendamento - 1]['data']

    horario = todas_consultas[numero_agendamento - 1]['hora']

    especialidade = todas_consultas[numero_agendamento - 1]['especialidade']

    print()
    
    print(f"Paciente:{nome_paciente['nome']}\nDia: {data}\nHora: {horario}\nEspecialidade: {especialidade}")

    print()

    print("Deseja:\n1 - Remarcar a consulta\n2- Cancelar consulta")

    print()

    escolha = input("Digite o número da escolha: ")

    if escolha == "1": 
        #Recebendo e validando a data da consulta.
        dia = selecao_data()

        if dia is None: 
            return 

        #Recebendo e e validando o horário da consulta.
        hora = selecao_horario(dia)

        if hora is None: 
            return 

        # Recebendo e validando escolha da especialidade.
        especialidade_escolhida = selecao_especialidade()

        if especialidade_escolhida is None: 
            return 

        consulta = {
            'data': dia,
            'hora': f"{int(hora) + 7}:00",
            'especialidade': especialidade_escolhida
        }

        #Atualizando o registro. 
        update_consulta(nome_paciente ['telefone'], data, horario, consulta)
        print("Consulta remarcada!")
        input("Pressione Enter para continuar...")

    elif escolha == "2": 
        delete_consulta(nome_paciente ['telefone'], data, horario)
        print("Consulta cancelada!")
        input("Pressione Enter para continuar...")