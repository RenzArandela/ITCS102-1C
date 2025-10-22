
anime_list = []  # create an empty list to store anime titles

while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ")
    if anime.lower() == "exit":
        break
    anime_list.append(anime)
    print(f"'{anime}' has been added to your anime list.")

print("\nYou have exited the anime entry program.")
print("Your anime list includes:")
for a in anime_list:
    print(f"- {a}")
