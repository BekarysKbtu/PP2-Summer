import re

txt = input("Введите строку: ")
checker = r"[a-z]+\_[a-z]+"

result = re.findall(checker, txt)

if result:
    print(f"Найдено: {result}")
else:
  print("Ничего не найдено")