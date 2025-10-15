import random

random_value = random.randint(1,5)
tries = 0
loop = True


name = input("Input your name --> ")
while loop == True:
    num = eval(input("Guess a number from 1 to 5 -- >"))

    if num == random_value:
        tries += 1
        print("winner !!!")
        break
    else:
        print("incorrect guess ")
        continue

print (f"HI {name}, Your Guess is Correct, Number of tries {tries}")
