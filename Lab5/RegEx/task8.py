import re

txt = input("Введите строку: ")
parts = re.findall(r'[A-Z][a-z]*', txt)

print("Результат:", parts)
