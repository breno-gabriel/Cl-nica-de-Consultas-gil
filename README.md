# Clínica de Consultas Ágil

Esse repositório é dedicado ao desafio proposto na segunda etapa do processo seletivo da Aceleradora Ágil da PUCRS e foi dividido da seguinte forma:

- database
    - consulta.csv
    - pacientes.csv
    - database.py
- funcionalidades
    - cadastro_consulta.py
    - cadastro_paciente.py
    - cancelar_remarcar_consulta.py
- utils
    - funcoes_uteis.py
- main.py

## Database 

 Esse diretório tem como objetivo armazenar arquivos relacionados a persistência de dados do programa. 

### consultas.csv e pacientes.csv

Esses dois arquivos simulam tabelas de um banco de dados relacional. O arquivo pacientes.csv contém o nome do paciente e o seu número de telefone como colunas, sendo que o telefone cumpre o papel de chave primária. Por sua vez, o arquivo consultas.csv contém data, hora, especialidade e telefone como colunas, sendo que o telefone cumpre o papel de chave secundária. Em uma modelagem de banco de dados, essas "tabelas" teriam uma relação de um para muitos. 

 ### database.py

Esse arquivo armazena funções que simulam consultas em banco de dados. Nesse arquivo estarão presentes funções para criar, deletar, atualizar e ler registros dos arquivos consultas.csv e pacientes.csv. 

 ## funcionalidades

 ### cadastro_consulta.py

Nesse arquivo, está presente o código responsável por realizar o cadastro das consultas dos pacientes na Clínica Ágil. Aqui são recebidas as entradas (paciente, data, hora, especialidade), realizada validações e o armazenamento no arquivo consultas.csv. Quanto a implementação, é gerada uma lista numerada dos pacientes, como solicitado nos requisitos, a data digitada pelo usuário, para o horário, é gerado uma lista numerada de horas, que vão das 8:00 ate às 20:00, contendo os horários disponíveis para agendamento de consulta em um determinado dia (devido a isso, se exister outro paciente agendado para um determinado horário, esse horário não aparecerá na lista), para as especialidades, optei por retornar uma lista numerada contendo 17 áreas médicas e solicitar que o usuário escolha uma delas para a consulta. Tudo ocorrendo bem, o usuário receberá uma mensagem de confirmação e retornará para o menu inicial. Caso contrário, receberá uma mensagem de falha e retornará ao menu inicial. 

 ### cadastro_paciente.py

Nesse arquivo, está presente o código que é responsável por cadastrar o paciente no sistema da clínica. O programa solicita ao usuário o nome e número de telefone (realizando validação desse número para que tenha 9 caracteres númericos, sendo o primeiro 9). Em seguida, é verificado se o número de telefone está cadastrado ou não. 

 ### cancelar_remarcar_consulta.py

Nesse arquivo, está toda a lógica para realizar a remarcação ou cancelamento de uma consulta. Tudo começa com o programa exibindo uma lista de pacientes cadastrados, frutos de uma consulta no arquivo pacientes.csv. Em seguida, é solicitado que o usuário escolha um número. Em seguida, o usuário poderá escolher se deseja remarcar ou cancelar a consulta. Se desejar remarcar, será solicitada a nova data, horário e especialidade. Se desejar cancelar, receberá uma mensagem de confirmação do cancelamento. 

## Utils 

### funcoes_uteis.py

Nesse arquivo, estão presentes funções que serão utilizadas por uma ou mais funcionalidades. O motivo disso é aumentar a modularidade do código, permitindo reuso, organização e facilitando a manutenção. É por esse motivo que também dividi as funcionalidades em três arquivos. 

## main.py

Esse é o arquivo principal do programa. Nele temos o menu e a chamada para as funções relacionadas às outras funcionalidades. Eis o coração do programa. 

É Interessante notas que busquei atribuir cores às mensagens do terminal. Amarelo para instruções, verde para mensagens de confirmação, vermelho para erros e azul para opções de lista.  