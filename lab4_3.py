#3. Create one list of elements and take specific element and position of element from
#user and add that element at that position.
my_list = [10, 20, 30, 40, 50]

element = int(input("Enter element to add: "))
position = int(input("Enter position: "))

my_list.insert(position, element)
print("Updated List:", my_list)
