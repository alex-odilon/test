"""
Este módulo contém funções para processar arquivos e realizar divisões.
A função 'process_file' lê um arquivo e retorna seu tamanho, enquanto 'divide_numbers'
realiza uma divisão entre dois números e trata a divisão por zero.
"""


def process_file(file_path):
    """
    Lê o conteúdo de um arquivo e imprime seu conteúdo.

    :param file_path: Caminho do arquivo a ser processado.
    :return: O tamanho do conteúdo lido do arquivo.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()
        print(data)
    return len(data)


def divide_numbers(a, b):
    """
    Realiza a divisão de dois números e trata a divisão por zero.

    :param a: O numerador da divisão.
    :param b: O denominador da divisão.
    :return: O resultado da divisão ou uma mensagem de erro em caso de divisão por zero.
    """
    if b == 0:
        return "Error: Division by zero"
    return a / b


result = divide_numbers(10, 0)
print("Result is:", result)
