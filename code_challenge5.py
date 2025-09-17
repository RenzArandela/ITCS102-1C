value = eval(input("Type a number: "))
result = 1

for y in range(value, 0, -1):
    result *= y

print("Factorial of", value, "is", result)
