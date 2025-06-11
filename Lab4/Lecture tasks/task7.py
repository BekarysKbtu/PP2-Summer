import datetime

x = datetime.datetime(2025,5,28)
y = datetime.datetime.now()
passed_day = int(y.strftime("%j")) - int(x.strftime("%j"))

print(365 - passed_day)





