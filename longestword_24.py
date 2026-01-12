#24. Find the length of the longest word in a sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
max_length = max(len(word) for word in words)  # find the max length
print("Length of the longest word is:", max_length)
