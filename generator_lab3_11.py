# Write a generator that yields numbers from 1 to 10.(lab3-11)
def numbers_1_to_10():
    for i in range(1, 11):
        yield i
for num in numbers_1_to_10():
    print(num)


