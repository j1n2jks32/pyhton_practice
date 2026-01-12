#22. Find the length of a string without using len().
text=input("enter a text")
count=0
for char in text:
    count+=1

print("Length of the string is:", count)
