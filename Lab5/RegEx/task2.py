import re

txt = input("Введите строку: ")
checker = r"^ab{2,3}$"

result = re.search(checker, txt)

if result:
    print("Yes")
else:
    print("No")

    