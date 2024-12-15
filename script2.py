from typing import Optional

"""
Este módulo contém funções para contar o número de linhas em um arquivo
e multiplicar dois números. A função count_lines tenta abrir um arquivo e
contar o número de linhas. Se houver erro, retorna None.
"""


def count_lines(file_path: str) -> Optional[int]:
    """
    Conta o número de linhas em um arquivo especificado por file_path.

    :param file_path: Caminho do arquivo a ser lido.
    :return: Número de linhas no arquivo ou None se ocorrer um erro.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        return len(lines)
    except FileNotFoundError as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return None
    except OSError as e:
        print(f"Erro ao acessar o arquivo: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None


def multiply_numbers(a: int, b: int) -> int:
    """
    Multiplica dois números.

    :param a: Primeiro número.
    :param b: Segundo número.
    :return: Resultado da multiplicação.
    """
    return a * b


FILE_PATH = "example.txt"  # Alterado para UPPER_CASE como constante
lines_count = count_lines(FILE_PATH)
print(f"O número de linhas em {FILE_PATH} é {lines_count}")

RESULT = multiply_numbers(3, 7)  # Alterado para UPPER_CASE como constante
print(f"O resultado da multiplicação é: {RESULT}")
