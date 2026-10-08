import csv
import re


class FormatoInvalidoError(Exception):
    pass


def validar_email(email):
    return bool(re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email))


def validar_cpf(cpf):
    return bool(re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf))


def validar_telefone(telefone):
    return bool(re.match(r"^\d{2}\s?\d{4,5}-\d{4}$", telefone))


def validar_data(data):
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", data))


def analisar_arquivo():
    validos = []
    invalidos = []

    try:
       with open(r"c:\Users\pedro\OneDrive\Documentos\apython\entregavel 5\dados.csv", "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            
            for linha in leitor:
                try:
                    if not validar_email(linha["email"]):
                        raise FormatoInvalidoError("E-mail inválido")

                    if not validar_cpf(linha["cpf"]):
                        raise FormatoInvalidoError("CPF inválido")

                    if not validar_telefone(linha["telefone"]):
                        raise FormatoInvalidoError("Telefone inválido")

                    if not validar_data(linha["data"]):
                        raise FormatoInvalidoError("Data inválida")

                    validos.append(linha)

                except FormatoInvalidoError as erro:
                    invalidos.append((linha["nome"], str(erro)))

    except FileNotFoundError:
        print("Erro: arquivo dados.csv não encontrado.")
    except KeyError as erro:
        print(f"Erro: coluna não encontrada: {erro}")
    except ValueError:
        print("Erro: valor inválido.")
    else:
        print("Arquivo lido com sucesso.")
    finally:
        print("Análise finalizada.")

    return validos, invalidos


# Programa principal
validos, invalidos = analisar_arquivo()

# Relatório
print("\n===== RELATÓRIO =====")
print(f"Total de registros: {len(validos) + len(invalidos)}")
print(f"Registros válidos: {len(validos)}")
print(f"Registros inválidos: {len(invalidos)}")

print("\n--- DADOS VÁLIDOS ---")
for pessoa in validos:
    print(
        f"Nome: {pessoa['nome']} | "
        f"E-mail: {pessoa['email']} | "
        f"CPF: {pessoa['cpf']} | "
        f"Telefone: {pessoa['telefone']} | "
        f"Data: {pessoa['data']}"
    )

print("\n--- DADOS INVÁLIDOS ---")
for nome, erro in invalidos:
    print(f"Nome: {nome} | Erro: {erro}")