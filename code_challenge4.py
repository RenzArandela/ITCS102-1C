print("Welcome to 1C Manga Selector")
print("Pick a genre:")
print("1. Action")
print("2. Horror")
print("3. Romance")

genre = input("Enter 1/2/3: ")

if genre == "1":
    print("You picked Action")
elif genre == "2":
    print("You picked Horror")
elif genre == "3":
    print("You picked Romance")

print("Pick a year range:")
print("1. 1990s")
print("2. 2000s")
print("3. 2010s")
year = input("Enter 1/2/3: ")

print("Pick length:")
print("1. Short")
print("2. Medium")
print("3. Long")
length = input("Enter 1/2/3: ")

if genre == "1" and year == "2" and length == "3":
    print("Recommended:")
    print("Fullmetal Alchemist")
    print("D.Gray-man")
    print("Gantz")
    print("Air Gear")
    print("Eyeshield 21")
else:
    print("No recommendations available")
