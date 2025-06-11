import datetime

x = datetime.datetime.now()

y = int(x.strftime("%d")) - 1
t = int(x.strftime("%d")) + 1

print("Yesterday's date: " , y, "-" , x.strftime("%m"), "-" , x.strftime("%Y"))
print("Today's date: " , x.strftime("%d"), "-" , x.strftime("%m"), "-" , x.strftime("%Y"))
print("Tomorrow's date: ", t, "-" , x.strftime("%m"), "-" , x.strftime("%Y"))