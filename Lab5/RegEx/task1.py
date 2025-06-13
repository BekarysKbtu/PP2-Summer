import re

txt = input("Введите строку: ")
checker = r"^ab*$"

result = re.search(checker, txt)

if result:
    print("Yes")
else:
    print("No")