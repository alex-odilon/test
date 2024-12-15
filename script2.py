def count_lines(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        return len(lines)
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return None


def multiply_numbers(a, b):
    return a * b


file_path = "example.txt"
lines_count = count_lines(file_path)
print(f"O número de linhas em {file_path} é {lines_count}")

result = multiply_numbers(3, 7)
print(f"O resultado da multiplicação é: {result}")
