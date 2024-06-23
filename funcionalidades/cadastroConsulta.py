from database.database import read_pacientes, create_consulta
from utils.funcoes_uteis import selecao_especialidade,selecao_data, selecao_horario, selecao_pacientes, RED, GREEN, YELLOW, BLUE, RESET


def cadastrarConsulta():

    #Recebendo o paciente escolhido.
    pacientesCadastrados = read_pacientes()
    
    pacienteEscolhido = selecao_pacientes(pacientesCadastrados)

    if pacienteEscolhido is None: 
        return None 

    print()

    #Recebendo e validando a data da consulta.
    data = selecao_data()

    if data is None:
        return 

    print()

    #Recebendo e e validando o horário da consulta.
    hora = selecao_horario(data)

    if hora is None: 
        return 

    print()

    # Recebendo e validando escolha da especialidade.
    especilidade_escolhida = selecao_especialidade()

    if especilidade_escolhida is None: 
        return 

    print()

    #Armazenando no banco de dados. 
    consulta = {
        'data': data,
        'hora': f"{int(hora) + 7}:00",
        'especialidade': especilidade_escolhida,
        'telefone': pacienteEscolhido['telefone']
    }

    create_consulta(consulta)
    print(f"{GREEN}Consulta agendada com sucesso!{RESET}")
    input(f"{YELLOW}Pressione Enter para continuar...{RESET}")