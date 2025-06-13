import re

txt = input("Введите строку: ")
checker = r"^a.*b$"

result = re.search(checker, txt)

if result:
    print("Yes")
else:
    print("No")
