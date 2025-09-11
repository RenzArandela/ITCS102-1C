temp = int(input("Enter temperature: "))

if temp >= 1 and temp <= 20:
    print("It is very cold")
elif temp >= 21 and temp <= 30:
    print("It is a bit cold")
elif temp >= 31 and temp <= 37:
    print("Temperature is normal")
elif temp >= 38 and temp <= 45:
    print("It feels hot")
elif temp >= 46 and temp <= 50:
    print("It is boiling hot")
elif temp > 50:
    print("Danger! Too hot")
else:
    print("Invalid temperature")
