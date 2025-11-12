def Greetwithname(name):
    print(f"Hello{name}, Hoyyyyyyyyyyyyyy") 

def FunctionwithReturn(number):
        print(f"this function calculates the summation from 1 to {number}")
        sum = 0
        for x in range (1, number +1, 1):
            sum += x
        return sum
    
def Greetperson(name, loc, age):
        print(f"Hello {name}, from {loc}, {age} yr\s old")

def Factorial(number):
    print(f"This function calculates the factorial of {number}")
    fact = 1
    for x in range(1, number + 1):
        fact *= x
    return fact


    
