Desafio Sprint 5 - Python

Projeto desenvolvido para a atividade de Desenvolvimento em Python.

O que o projeto faz

O programa lê um arquivo dados.csv e verifica se os dados estão corretos.

São validados:

E-mail
CPF
Telefone
Data

As validações são feitas utilizando Regex com o módulo re.

Tratamento de erros

O programa utiliza:

FileNotFoundError
ValueError
KeyError
try
except
else
finally

Também foi criada uma exceção personalizada chamada FormatoInvalidoError.

Arquivos
app.py
dados.csv
README.md

Como executar

Com o Python instalado, execute no terminal:

python app.py


O programa mostra um relatório informando:

Total de registros
Registros válidos
Registros inválidos
Motivo dos dados inválidos
Exemplo
===== RELATÓRIO =====
Total de registros: 4
Registros válidos: 3
Registros inválidos: 1