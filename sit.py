# readings = [12, -3, 8, -1, 20, 5]

# total = 0

# for value in readings:
#     if value > 0:
#         continue
#     total += value

# print(f"The total of the negative readings is: {total}")


for row in range(3):
    for col in range(4):
        print(f"({row}, {col})")


print('\n')

numbers = range(1, 11) 
for number in numbers: 
    if number % 2 == 0: 
        continue 
    print(number)

print('\n')

words = ["This", "is", "Nihal", "STOP", "Computer", "Scientist"]

for word in words:
    print(word)

    if word == "STOP":
        break

print('\n')

for i in range(3):
    try:
        number = int(input("Enter a number: "))
        print("You entered:", number)

    except ValueError:
        print("Invalid input. Please enter a number.")

print('\n')

data = [10, 'nihal', 677, "hyder", 30] 
total = 0 
for item in data: 
    try: 
        total += int(item) 
    except ValueError: 
        print("Invalid value:", item) 
        continue 
    print("Total:", total)