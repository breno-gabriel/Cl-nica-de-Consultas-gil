from database.database import read_pacientes, create_consulta, ler_consultas_por_data

def validar_horario(horario): 

        try:
            hora_int = int(horario + 7)
            if 1 <= hora_int <= 13:
                return True
            else:
                return False 
        except ValueError:
                return False 


from datetime import datetime

def validar_data(data):
    try:
        data_valida = datetime.strptime(data, "%d/%m/%y")
        return data_valida
    except ValueError:
        return None

# Função para validar o horário
def validar_horario(horario):
    try:
        hora_int = int(horario)
        if 8 <= hora_int <= 20:
            return True
        else:
            return False
    except ValueError:
        return False

def cadastrarConsulta():
    especialidades = [
        "Cardiologia", "Dermatologia", "Endocrinologia", "Gastroenterologia",
        "Geriatria", "Ginecologia", "Hematologia", "Infectologia",
        "Nefrologia", "Neurologia", "Oftalmologia", "Ortopedia",
        "Otorrinolaringologia", "Pediatria", "Psiquiatria", "Reumatologia", "Urologia"
    ]

    #Recebendo o paciente escolhido.
    pacientesCadastrados = read_pacientes()

    for i, paciente in enumerate(pacientesCadastrados, start=1):
        print(f"{i} - {paciente['nome']}")

    numPacienteEscolhido = int(input("Escolha um número correspondente a um paciente: "))
    
    if numPacienteEscolhido > len(pacientesCadastrados) or numPacienteEscolhido <= 0:
        print("O número digitado não está relacionado a nenhum paciente.")
        return 
    
    pacienteEscolhido = pacientesCadastrados[numPacienteEscolhido - 1]

    #Recebendo a data da consulta.
    data = input("Digite a data da consulta no formato dd/mm/yy: ")

    data_valida = validar_data(data)
    if not validar_data(data):
        print("Por gentileza, digite a data no formato dd/mm/yy.")
        return 

    # Verifica se a data do agendamento não é anterior ao dia atual
    if data_valida.date() < datetime.now().date():
        print("Erro: A data do agendamento não pode ser anterior ao dia atual.")
        return 

    #Verificando se existem horários disponíveis para essa data. 
    horarios_disponíveis = ler_consultas_por_data(data)

    if len(horarios_disponíveis) == 0: 
        print("Desculpe! Mas não temos nenhum horários disponível para esse dia :()")

    #Recebendo o horário da consulta.
    for i, j in enumerate(horarios_disponíveis):
        print(f"{i + 1} - {j}")

    hora = int(input("Digite o número relacionado a um horário para a consulta: "))

    if not validar_horario(hora + 7):
        print("Por gentileza, digite um horário válido.")
        return 

    # Recebendo escolha da especialidade.
    for i, especialidade in enumerate(especialidades, start=1):
        print(f"{i} - {especialidade}")

    escolhaEspecialidade = int(input("Digite o número relacionado a uma de nossas especialidades: "))

    if escolhaEspecialidade < 1 or escolhaEspecialidade > len(especialidades):
        print("Escolha inválida.")
        return

    especialidadeEscolhida = especialidades[escolhaEspecialidade - 1]

    #Armazenando no banco de dados. 
    consulta = {
        'data': data_valida.strftime("%d/%m/%y"),
        'hora': f"{int(hora) + 7}:00",
        'especialidade': especialidadeEscolhida,
        'telefone': pacienteEscolhido['telefone']
    }

    create_consulta(consulta)
    print("Consulta agendada com sucesso!")