from Card import card
from hint import answer
from deckbuilder import Deck
import random
import sys

def start():
    print("you will be playing a game that will ask you to guess a card in a standard 52 card deck")
    print("enter y to play or n to not play")
    repeat = True
    while repeat == True:
        decide = input()
        decide = decide.lower()
        if decide == "y":
            repeat = False
        elif decide == "n":
            sys.exit("why did you even use this app?")
        else:
            pass
    game()

pile = Deck()

def game():
    Hints = 3
    rand = random.randint(0,len(pile))
    drew = pile[rand]



start()