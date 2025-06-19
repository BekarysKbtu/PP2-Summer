import datetime

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

entry = input("Write your journal entry:\n")

with open("journal.txt", "a") as file:
    file.write(f"\n[{timestamp}]\n")
    file.write(entry + "\n")

print("Your entry has been saved to journal.txt.")
