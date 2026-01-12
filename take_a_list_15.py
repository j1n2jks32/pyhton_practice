#15 . Take a list of numbers and print only even numbers on the console.

# Take input from user, separated by spaces
numbers = input("Enter numbers separated by space: ").split()

# Convert each input to integer
numbers = [int(num) for num in numbers]

# Loop through the list and print only even numbers
for num in numbers:
    if num % 2 == 0:
        print(num)
