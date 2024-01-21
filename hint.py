from Card import card

def answer(hidden):
    if hidden.value % 2 != 0:
        print("card is odd")
    else:
        print("card is even")
