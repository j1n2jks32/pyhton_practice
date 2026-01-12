# Write a generator function to yield even numbers up to 20 (lab3-12)
def even_numbers_upto_20():
    for i in range(2, 21, 2):
        yield i
for num in even_numbers_upto_20():
    print(num)
