import datetime

date1 = datetime.datetime(2025, 6, 11, 12, 0, 0)
date2 = datetime.datetime(2025, 6, 11, 12, 30, 45)

diff = date2 - date1
seconds = diff.total_seconds()

print(f"Difference in seconds: {seconds}")
