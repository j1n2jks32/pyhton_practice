def sum_of_numbers(*args):
    total=0
    for num in args:
        total+=num
    return total
result=sum_of_numbers(10,10,20,20)
print("sum of numbers",result)
