
anime_lists = [ ]

while True:
    title = input("Enter the title of an anime (type 'exit' to finish): ")

    if title == "exit":
        print("You have exited the anime program")
        break
    else:
        anime_lists.append(title)
        print(f"'{title}' has been successfully added to your anime list.")

print("Your anime list includes:")
for anime in anime_lists:
        print(f" - {anime}")
