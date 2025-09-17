print("ODD NUMBER ACCUMULATOR")
print("Enter 10 numbers. We'll sum only the odd ones!")
print()

total = 0

for i in range(10):
    num = eval(input("Enter a number: "))
    if num % 2 == 1:
        total = total + num

print()
print("Sum of all odd numbers:", total)
