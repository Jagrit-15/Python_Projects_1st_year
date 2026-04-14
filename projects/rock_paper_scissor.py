import random
user = int(input("What is your choice, 0 = rock, 1 = paper, 2 = scissor : "))
comp = random.randint(0,2)
game = ["rock","paper","scissor"]
print(f"You chose : {game[user]}\tComputer chose : {game[comp]}")
if(user == comp) :
    print("Draw")
elif(user == 0 and comp == 1):
    print("You lose")
elif(user == 0 and comp == 2):
    print("You win")
elif(user == 1 and comp == 0):
    print("You win")
elif(user == 1 and comp == 2):
    print("You lose")
elif(user == 2 and comp == 0):
    print("You lose")
elif(user == 2 and comp == 1):
    print("You win")
else:
    print("Invalid Input")