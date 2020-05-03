
import random

Playing = 'Yes' 
bal = 1000
bet = 0
suits = ["Spades", "Clubs","Hearts","Diamonds"]

ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
values = {"Ace":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":10,"Queen":10,"King":10}


#################### Card Class #######################

class Card():
    def __init__(self,suit,rank,value):
        self.rank = rank
        self.suit = suit
        self.value= value
    def __str__(self):
        return  self.rank+" of "+self.suit


####################### Deck Class #########################

class Deck():
    def __init__(self):
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(Card(s,r,value=r))
    def __str__(self):
        deckComp = ""
        for c in self.deck:
            deckComp +='\n'+c.__str__()
        return "the deck has: "+deckComp

    def dealfromdeck(self):
        singleCard = self.deck.pop()
        return singleCard
    def shuffle(self):
        random.shuffle(self.deck)


########################## Player Class ################

class Player():

    def __init__(self,total=1000,bot=False):
        self.total = total
        self.hand = []
        self.bet = 0
        self.aces = 0
        self.value = 0
        self.bot = bot
    def __str__(self):
        pri='Your total is {}\nYour current bet is {}\nYour value is {}'.format(self.total,self.bet,self.value)+'\nYour hand is \n'+'\n'.join(map(str,self.hand))
        return pri
    def __repr__(self):
        return str(self)

    def take_bet(self):
        self.bet=input("Enter your bet amount ")
        print(f'{self.bet} is how much u bet')

    def checkAce(self):
        if self.value > 21 and self.aces:
            self.value -=10
            self.aces -=1
    def deal(self,card):
        self.hand.append(card)
        self.value += values[card.value]
        if card.rank == "Ace":
            self.aces += 1
    def showHand(self):
        if self.bot:
            print("-------------------------------")
            print("\nThis the botss hand ")
            print(*self.hand, sep =", ")
            print("Value is: "+str(self.value)+"\n----------------------------")
        else:
            print("This the players hand ")
            print(*self.hand, sep =", ")
            print("Value is: "+str(self.value)+"\n----------------------------")

############### Important Functions #######################


def checkWin(b,a,bet):
    global bal
    if a>21:
        print("player busted bot won :( ")
        bal-=bet
        print(bal)
        return bal
    if b>21:
        print("bot bustesd player won :) ")
        bal+=bet
        print(bal)
        return bal
    if b>a:
        print("bot won, the bot had a value of {}, while ur value was {} :( ".format(b,a))
        bal-=bet
        print(bal)
        return bal
    elif a>b:
        print("Player won, the bot had a value of {}, while ur value was {} :)".format(b,a)) 
        bal+=bet
        print(bal)
        return bal
    else:
        print("tieee")
        return bal

def botTurn(bet):
    global bal
    if bot.value< aki.value:
        bot.deal(d.dealfromdeck())
        bot.checkAce()
        bot.showHand()
        botTurn(bet)
    else:
        checkWin(bot.value,aki.value,bet)

def decision(a,b,bet):
    global bal
    answer = input("enter what u wanna do. Type hit or stand ")
    if answer[0].lower() == 'h':
        print("U chose to hit")
        aki.deal(d.dealfromdeck())
        aki.checkAce()
        aki.showHand()
        if aki.value<=21:
            decision(a,b,bet)
        else:
            print("game over u busted")
            bal-=bet
            print(bal)
            return
    else:
        botTurn(bet)

def takebet():
    global bal
    bet = input("How much u wanna bet, ur balance is {} ".format(bal))
    if  int(bet)>bal:
        print("bet too high, your balance is {}".format(bal))
        takebet()
    else:
        return int(bet)


######################### Start Game ################


while Playing[0].lower() == 'y' and bal >0:
    print("Welcome to Blackjack")
    d = Deck()
    aki = Player()
    bot = Player(bot=True)
    d.shuffle()
    aki.deal(d.dealfromdeck())
    bot.deal(d.dealfromdeck())
    aki.deal(d.dealfromdeck())
    bet = takebet()
    bot.showHand()
    aki.showHand()
    decision(aki.value,bot.value,bet)
    Playing = input("u wanna play again? ")
    if bal<1:
        print("Go home kid, U have no balance. Game over")

