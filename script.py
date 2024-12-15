import os
import sys

def process_file(file_path):
    file = open(file_path, 'r')
    data = file.read()
    print(data)
    file.close()
    return len(data)

def divide_numbers(a, b):
    return a / b

result = divide_numbers(10, 0)
print("Result is:", result)
