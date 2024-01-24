from Card import card

def Deck():
    Types = ["Hearts","Spades","Clubs","Diamonds"]
    Names = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
    Value = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    deck = list()
    for item in Types:
        for index, each in enumerate(Names):
            single = card(each,Value[index],item)
            deck.append(single)
    return(deck)