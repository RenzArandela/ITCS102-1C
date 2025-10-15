name = input("Hi, What is your name? -->  ")

print ("++++++++++++++++++")
print()
print("ODD NUMBER SELECTION, press 0 to stop the loop")
print()
print("++++++++++++++++++++")

num = eval(input("Enter a random number --"))
sum = 0 
odd =- 3

while num != 0:

    if num % 2 != 0:
        print(f"{num} ODD NUMBER DETECTED")
        num = eval(input("Enter a random number --> "))
        sum += num 
        odd += str(num) + " "
    else:
        print(f"{num} EVEN NUMBER DETECTED")
        num = eval(input("Enter a random number -->"))
        continue

print(f"hi {name},the sum of all ODD number is {sum}")
print(f"ODD numbers include the ff --> {odd}")
