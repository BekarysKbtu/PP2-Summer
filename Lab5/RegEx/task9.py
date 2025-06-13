import re

txt = input("Введите строку: ")
spaced = re.sub(r'(?<!^)(?=[A-Z])', ' ', txt)

print("Результат:", spaced)
