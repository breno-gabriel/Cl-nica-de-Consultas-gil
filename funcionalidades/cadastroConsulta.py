from database.database import read_pacientes, create_consulta
from utils.funcoes_uteis import selecao_especialidade,selecao_data, selecao_horario, selecao_pacientes

# def validar_horario(horario): 

#         try:
#             hora_int = int(horario + 7)
#             if 1 <= hora_int <= 13:
#                 return True
#             else:
#                 return False 
#         except ValueError:
#                 return False 


def cadastrarConsulta():

    #Recebendo o paciente escolhido.
    pacientesCadastrados = read_pacientes()
    
    pacienteEscolhido = selecao_pacientes(pacientesCadastrados)

    #Recebendo e validando a data da consulta.
    data = selecao_data()

    #Recebendo e e validando o horário da consulta.
    hora = selecao_horario(data)

    # Recebendo e validando escolha da especialidade.
    especilidade_escolhida = selecao_especialidade()

    #Armazenando no banco de dados. 
    consulta = {
        'data': data,
        'hora': f"{int(hora) + 7}:00",
        'especialidade': especilidade_escolhida,
        'telefone': pacienteEscolhido['telefone']
    }

    create_consulta(consulta)
    print("Consulta agendada com sucesso!")