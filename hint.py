from Card import card

def answer(hidden):
    print("Enter 1 if you want to know if the card is odd or even")
    answered = False

    while answered == False:
        try:
            question = input()
            question = int(question)
            match question:
                case 1:
                    oddoreven(hidden)
                    answered = True
                case _:
                    print("number was not associated with a question please try again")
        except:
            print("answer was not a whole number please try again")


def oddoreven(var):
    if var.value % 2 != 0:
        print("your card is odd")
    else:
        print("your card is even")