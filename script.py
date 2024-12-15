def process_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        print(data)
    return len(data)


def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


result = divide_numbers(10, 0)
print("Result is:", result)
