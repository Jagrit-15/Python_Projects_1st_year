import random
import sys
print('''
          _____
         |A .  | _____
         | /.\ ||A ^  | _____                /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$          /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$
         |(_._)|| / \ ||A _  | _____        | $$__  $$| $$       /$$__  $$ /$$__  $$| $$  /$$/         |__  $$ /$$__  $$ /$$__  $$| $$  /$$/
         |  |  || \ / || ( ) ||A_ _ |       | $$  \ $$| $$      | $$  \ $$| $$  \__/| $$ /$$/             | $$| $$  \ $$| $$  \__/| $$ /$$/ 
         |____V||  .  ||(_'_)||( v )|       | $$$$$$$ | $$      | $$$$$$$$| $$      | $$$$$/              | $$| $$$$$$$$| $$      | $$$$$/  
                |____V||  |  || \ / |       | $$__  $$| $$      | $$__  $$| $$      | $$  $$         /$$  | $$| $$__  $$| $$      | $$  $$  
                       |____V||  .  |       | $$  \ $$| $$      | $$  | $$| $$    $$| $$\  $$       | $$  | $$| $$  | $$| $$    $$| $$\  $$ 
                              |____V|       | $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/| $$ \  $$      |  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$
                                            |_______/ |________/|__/  |__/ \______/ |__/  \__/       \______/ |__/  |__/ \______/ |__/  \__/
                                                                                                
                                                                                                
                ''')

cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
values = {"A" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, 
          "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10}

def get_score(hand):
    """Calculates score and handles Ace flipping from 11 to 1."""
    score = sum(values[c] for c in hand)
    aces = hand.count("A")
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

comp = [random.choice(cards), random.choice(cards)]
player = [random.choice(cards), random.choice(cards)]

print(f"Computer : {comp[0]}")
print(f"User : {player} (Total: {get_score(player)})")

# User's Turn
choice = input("Do you want to take more cards 'yes' or 'no' : ").lower()

while choice == "yes":
    player.append(random.choice(cards))
    current_sum = get_score(player)
    print(f"Your hand: {player} (Total: {current_sum})")

    if current_sum > 21:
        print("You lose since your sum was more than 21")
        sys.exit(0)
    else:
        choice = input("Do you want to take more cards 'yes' or 'no' : ").lower()

# Computer's Turn
while get_score(comp) < 17:
    comp.append(random.choice(cards))

sum_user = get_score(player)
sum_comp = get_score(comp)

print("\n--- FINAL RESULTS ---")
print(f"COMP : {comp} (Total: {sum_comp})")
print(f"PLAYER : {player} (Total: {sum_user})")

if sum_comp > 21:
    print("Computer Busted! You Won!")
elif sum_user > sum_comp:
    print("You Won!")
elif sum_user == sum_comp:
    print("It's a Push (Tie)!")
else:
    print("You Lost!")