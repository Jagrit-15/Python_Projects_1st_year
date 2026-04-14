import random
print(''' 
  _   _                                                   ____                      
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __           / ___| __ _ _ __ ___   ___ 
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \         | |  _ / _` | '_ ` _ \ / _ \
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |        | |_| | (_| | | | | | |  __/
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|         \____|\__,_|_| |_| |_|\___|
                    |___/                                                           
''')

# Hangman Game Word Lists

space_and_astronomy = [
    "Moon", "Earth", "Rocket", "Planet", "Sun", 
    "Alien", "Stars", "Spaceship", "Rover", "Mars", 
    "Astronaut", "Sky", "Comet", "Solar", "Telescope"
]

tropical_destinations = [
    "Beach", "Ocean", "Palm", "Boat", "Summer", 
    "Sand", "Wave", "Swim", "Shell", "Island", 
    "Sun", "Trip", "Fish", "Coral", "Water"
]

kitchen_and_culinary = [
    "Spoon", "Plate", "Knife", "Fork", "Oven", 
    "Cook", "Bowl", "Food", "Bread", "Salt", 
    "Glass", "Pan", "Stove", "Chef", "Cup"
]

technology = [
    "Phone", "Laptop", "Screen", "Mouse", "Game", 
    "Robot", "Typing", "Online", "Video", "Email", 
    "Sound", "Music", "Smart", "Power", "Cable"
]

sports_and_athletes = [
    "Cricket", "Soccer", "Tennis", "Player", "Stadium", 
    "Batting", "Bowling", "Coach", "Winner", "Hockey", 
    "Runner", "Match", "Team", "Score", "Ball"
]

category = [space_and_astronomy, tropical_destinations, kitchen_and_culinary, technology, sports_and_athletes]
category_name = ["space_and_astronomy", "tropical_destinations", "kitchen_and_culinary", "technology", "sports_and_athletes"]
cat_num = random.randint(0,4)
selected_category = category[cat_num]
print(f"YOUR CATEGORY IS : {category_name[cat_num]}")
selected_word = random.choice(selected_category).lower()
length_of_word = len(selected_word)

life = 6
word_guessed = ["_"] * length_of_word
for i in range(length_of_word):
    print("_", end=" ")
print("")
print(f"LIVES : {life}")
while(life !=0 and "".join(word_guessed) != selected_word):

    char_guessed = input("Guess a letter : ").lower()
    check = 0

    for i in range(length_of_word):
        if(char_guessed == selected_word[i]):
            word_guessed[i]=char_guessed
            check+=1

    for i in range(length_of_word):
        print(word_guessed[i],end=" ")
    print("")
    if(check == 0):
        print("Wrong Guess")
        life-=1
        print(f"Lives = : {life}")

if("".join(word_guessed) == selected_word):
    print("YOU WON")

        