import time

print("COUNTDOWN TIMER SIMULATOR")

start = eval(input("Enter the starting number for countdown: "))

print()
print("Countdown started:")

for i in range(start, 0, -1):
    print(i)
    time.sleep(0.5)

time.sleep(0.5)
print("Liftoff!")
