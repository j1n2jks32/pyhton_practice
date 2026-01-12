# Write a generator that yields characters of a string one by one.(lab3-13)
def string_chars(s):
    for ch in s:
        yield ch
for c in string_chars("Python"):
    print(c)
