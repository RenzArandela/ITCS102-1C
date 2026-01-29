word = input("Enter a word: ")

length = len(word)
total = 0

for i in range(1, length + 1):
    value = i * 2
    print(f"{i}:{value}")
    total += value

average = total / length

print("The average is", average)

if length > average:
    print(f'This "{word}" has more than the average')
elif length < average:
    print(f'This "{word}" has less than the average')
else:
    print(f'This "{word}" is equal to the average')
