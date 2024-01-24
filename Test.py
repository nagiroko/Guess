from Card import card
from hint import answer
from deckbuilder import Deck
import random

deck = Deck()
rand = random.randint(0,len(deck))
single = deck[rand]
answer(single)

