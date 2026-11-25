import json

with open("jikan.json", "r", encoding="utf-8") as f:
    data = json.load(f)

anime_list = data["data"]   # a list of 25 anime (each one is a dictionary)


# ------------------------------------------------------------
# Q1. Filtering and counting
# Print the title and score of every anime with a score
# greater than 9.0. Then print how many there were.
# ------------------------------------------------------------
def titlescore(x, y):
    great = int
    great = 0
    for name in range(x, y):
        if anime_list[name]["score"] > 9.0:
            print(anime_list[name]["title"])
            print(anime_list[name]["score"])
            great += 1
    print(f"There are {great} anime with a score of above 9.00. ")

titlescore(0, len(anime_list))



# ------------------------------------------------------------
# Q2. Accumulator
# Calculate and print the average score of all the anime
# in the list. Round the answer to 2 decimal places.
# ------------------------------------------------------------
def average(x, y):
    divide = 0
    total = 0
    for add in range(x, y):
        total += anime_list[add]["score"]
        divide += 1
    print(f"The average score of all the anime in this list is {total / divide:.2f}. ")

average(0, len(anime_list))



# ------------------------------------------------------------
# Q3. Finding the maximum
# Print the title and episode count of the anime that has the
# most episodes.
# Hint: look closely at the "episodes" values. Does every
# anime have a number?
# ------------------------------------------------------------
def maximum(x, y):
    winner = []
    for high in range(x, y):
        if anime_list[high]["episodes"] is not None:
            winner.append(anime_list[high]["episodes"])
    for high in range(x, y):
        if max(winner) == anime_list[high]["episodes"]:
            print(f"The anime with the most episodes is {anime_list[high]['title']} with {anime_list[high]['episodes']} episodes. ")
maximum(0, len(anime_list))
                
            



# ------------------------------------------------------------
# Q4. Nested lists
# Each anime has a "genres" list. Each item in that list is a
# dictionary with a "name" key (for example, "Comedy").
# Print the title of every anime that has the genre "Comedy".
# -----------------------------------------------------------
def find(x, y):
    for genre in range(x, y):
        for ah in range(len(anime_list["genres"])):
            print(anime_list[genre]["genres"][ah]['name'])


find(0, len(anime_list))