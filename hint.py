from Card import card

def answer(hidden):
    print("Enter 1 if you want to know if the card is odd or even")
    print("Enter 2 if you want to know the card's color")
    print("Enter 3 if you want to know the card's gender")
    print("Enter 4 if you want to know if the card is less than, greater than or equal to five")
    answered = False
    text = ""

    while answered == False:
        try:
            question = input()
            question = int(question)
            match question:
                case 1:
                    oddoreven(hidden)
                    answered = True
                case 2:
                    redorblack(hidden)
                    answered = True
                case 3:
                    gender(hidden)
                    answered = True
                case 4:
                    five(hidden)
                    answered = True
                case _:
                    print("number was not associated with a question please try again")
        except:
            print("answer was not a whole number please try again!")
    input("press enter to continue when ready")


def oddoreven(var):
    if var.value % 2 != 0:
        print("your card is odd")
    else:
        print("your card is even")

def redorblack(var):
    if var.type == "heart" or var.type == "diamond":
        print("card is red")
    else:
        print("card is black")

def gender(var):
    if var.name == "Queen":
        print("card is female")
    elif var.name == "King" or var.name == "Jack":
        print("card is male")
    else:
        print("gender is unconfirmed")
def five(var):
    if var.value > 5:
        print("card value is greater than five")
    elif var.value < 5:
        print("card value is less than five")
    elif var.value == 5:
        print("card value is five")
