# Write a generator that take a string (in any case: lower, mixed, etc.) and yield each 
#character in uppercase.(lab3-15)
def uppercase_chars(s):
    for ch in s:
        yield ch.upper()
for c in uppercase_chars("PyThOn"):
    print(c)
