import re

filename = 'journal.txt'

try:
    with open(filename, 'r') as file:
        content = file.read()

    entries = re.split(r'\n\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]\n', content)

    dates = re.findall(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]', content)

    count = len(dates)

    print(f"Number of entries: {count}")

    if count == 0:
        print("No entries found.")
    else:
        last_date = dates[-1]
        last_entry = entries[-1].strip()

        print("\nMost recent entry:")
        print(last_date)
        print(last_entry)

except FileNotFoundError:
    print(f"File '{filename}' not found.")
