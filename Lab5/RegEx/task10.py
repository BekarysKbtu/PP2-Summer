import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str

camel_input = input("Введите строку в camelCase: ")
snake_output = camel_to_snake(camel_input)
print("snake_case:", snake_output)
