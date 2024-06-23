import csv
from datetime import datetime


#CRUD paciente 
def create_paciente(paciente, filename='database/pacientes.csv'):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        file.seek(0, 2)  # Move o cursor para o final do arquivo
        if file.tell() == 0:  # Verifica se o arquivo está vazio
            fieldnames = ['nome', 'telefone']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Escreve os cabeçalhos apenas se o arquivo estiver vazio
        writer = csv.DictWriter(file, fieldnames=paciente.keys())
        writer.writerow(paciente)

def get_paciente_by_telefone(telefone, filename='database/pacientes.csv'):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == telefone:  
                paciente = {
                    'nome': row[0], 
                    'telefone': row[1]  
                }
                return paciente
    return None

def get_paciente_by_telefone(telefone, filename='database/pacientes.csv'):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['telefone'] == telefone:  
                paciente = {
                    'nome': row['nome'], 
                    'telefone': row['telefone']  
                }
                return paciente
    return None
    
def read_pacientes(filename='database/pacientes.csv'):
    pacientes = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            paciente = {
                'nome': row['nome'],  
                'telefone': row['telefone']  
            }
            pacientes.append(paciente)
    return pacientes

def delete_paciente(target_telefone, filename='database/pacientes.csv'):
    deleted = False
    rows = read_pacientes(filename)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        for row in rows:
            if row['telefone'] != target_telefone:
                writer.writerow(row)
            else:
                deleted = True
    return deleted

#CRUD consulta 

def create_consulta(consulta, filename='database/consultas.csv'):
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            file_exists = next(reader, None) is not None  
    except IOError as e:
        return

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['data', 'hora', 'especialidade', 'telefone']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  

        try:
            writer.writerow(consulta)
        except Exception as e:
            print(f"Erro ao tentar escrever no arquivo: {e}")

def ler_consultas_por_data(data, filename='database/consultas.csv'):
    horarios_possiveis = [f"{hora}:00" for hora in range(8, 21)]

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for consulta in reader:
            val = consulta['data']
            if consulta['data'] == data:
                horarios_possiveis.remove(consulta['hora'])

    # horarios_disponiveis = [hora for hora in horarios_possiveis if hora not in horarios_ocupados]
    return horarios_possiveis

def read_consultas(filename='database/consultas.csv'):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def update_consulta(target_telefone, target_data, target_hora, new_data, filename='database/consultas.csv'):
    updated = False
    fieldnames = ['data', 'hora', 'especialidade', 'telefone', 'nome']
    
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in rows:
            if row['telefone'] == target_telefone and row['data'] == target_data and row['hora'] == target_hora:
                # Atualiza apenas os campos necessários, mantendo o nome do paciente
                for key in new_data:
                    if key != 'nome':
                        row[key] = new_data[key]
                updated = True
            writer.writerow(row)
    
    return updated

def delete_consulta(target_telefone, target_data, target_hora, filename='database/consultas.csv'):
    deleted = False
    rows = read_consultas(filename)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        for row in rows:
            if not (row['telefone'] == target_telefone and row['data'] == target_data and row['hora'] == target_hora):
                writer.writerow(row)
            else:
                deleted = True
    return deleted