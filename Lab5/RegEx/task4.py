import re

txt = input("Введите строку: ")
checker = r"[A-Z][a-z]+"

result = re.findall(checker, txt)

if result:
    print(f"Найдено: {result}")
else:
    print("Ничего не найдено")