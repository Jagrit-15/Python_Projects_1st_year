
from stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

def main():
    while no_beepers_present():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        elif left_is_clear():
            turn_left()
            move()
        else:
            turn_around()

    print("Sucessfully Reached")

        

if __name__ == "__main__":
    import random
    my_worlds = ["world1", "world2", "world3", "world4", "world5", "world6", "world7", "world8", "world9", "world10"]
    random_world = random.choice(my_worlds)
    run_karel_program(random_world)