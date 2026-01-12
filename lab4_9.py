#4. Write a Python program to convert a tuple of string values to a tuple of integer values.(lab4)
str_tuple = ('1', '2', '3', '4', '5')

int_tuple = tuple(int(x) for x in str_tuple)
print(int_tuple)
