#4. Create one list of numbers from 1 to 100 and create two separate lists those contain 
#odd numbers and even numbers separately.
numbers = list(range(1, 101))

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
