import datetime

x = datetime.datetime.now()
fda = int(x.strftime("%d")) - 5

print(f"0{fda}", "-" , x.strftime("%m"), "-",   x.strftime("%Y"))