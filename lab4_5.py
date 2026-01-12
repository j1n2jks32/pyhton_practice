#5. Take a list of numbers in the string format, convert those numbers into integer 
#format and get sum of all those list elements.
#list_char_num = [‘12’,’23’,’67’,’56’,’12’,’90’]
list_char_num = ['12', '23', '67', '56', '12', '90']

int_list = [int(num) for num in list_char_num]
total = sum(int_list)

print("Integer List:", int_list)
print("Sum:", total)
