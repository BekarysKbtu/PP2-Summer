import time
import math

number = float(input())
delay_ms = int(input())

time.sleep(delay_ms / 1000)
result = math.sqrt(number)

print(f"Square root of {int(number)} after {delay_ms} miliseconds is {result}")
