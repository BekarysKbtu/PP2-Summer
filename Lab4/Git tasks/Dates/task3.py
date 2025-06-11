import datetime

x = datetime.datetime.now()
clean_time = x.replace(microsecond=0)
print(clean_time)