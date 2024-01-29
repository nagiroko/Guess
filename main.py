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
    while Hints > 0:
        choice = input("enter y if you want a hint or n if you would like to guess\n you have "+ str(Hints) + " hints left.")
        choice = choice.lower()
        if choice == "y":
            answer(drew)
            Hints -= 1
        elif choice == "n":
            Hints = 0
        else:
            pass
    Answer(drew)

def Answer(thing):
    guessOne = input("enter type of card. Ex- Diamonds")
    guessOne = guessOne.lower()
    guessOne = guessOne.capitalize()
    guessTwo = input("guess name of card. Exs- One or Queen ")
    guessTwo = guessTwo.lower()
    guessTwo = guessTwo.capitalize()
    if guessOne == thing.type and guessTwo == thing.name:
        thing.Right()
    else:
        thing.Wrong()

    restart = input("enter nothing to play again or enter something to quit game")
    if restart == '':
        game()
    else:
        sys.exit("Thanks for playing")




start()