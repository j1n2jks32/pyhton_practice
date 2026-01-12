#14
movies = []

while True:
    name = input("Enter movie name (type 'stop' to finish): ")
    if name == "stop" or "Stop":
        break
    movies.append(name)

print("Movies entered:")
print(movies)
