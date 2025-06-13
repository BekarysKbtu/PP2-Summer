def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    camel_str = parts[0] + ''.join(word.capitalize() for word in parts[1:])
    return camel_str

snake_input = input("Введите строку в snake_case: ")
camel_output = snake_to_camel(snake_input)
print("CamelCase:", camel_output)
