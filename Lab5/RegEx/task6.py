import re

txt = input("Введите текст: ")
pattern = r"[ ,.]"

replaced = re.sub(pattern, ":", txt)
print("Результат:", replaced)
