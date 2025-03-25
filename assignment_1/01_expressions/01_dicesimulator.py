# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.


import random


def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)
    print("Die 1:", die1)
    print("Die 2:", die2)
    
    total: int = die1 + die2
    print("Total of two dice:", total)
    
# for i in range(3):
#     print(roll_dice())



def main():
    roll_dice()
    roll_dice()
    roll_dice()
    
main()
