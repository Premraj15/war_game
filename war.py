import random
suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}


class Card:
    def __init__(self,suits,ranks):
        self.suit=suits
        self.rank=ranks
        self.value=values[ranks]

    def __str__(self):
        return self.suit +" of " + self.rank

class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                cards=Card(suit,rank)
                self.all_cards.append(cards)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def delete_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    def remove(self):
        return self.all_cards.pop()

    def add_card(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
player_one=Player("one")
player_two=Player("two")

new_deck=Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_card(new_deck.delete_one())
    player_two.add_card(new_deck.delete_one())

game_on=True
rounds=0

while game_on:
    rounds+=1
    print(rounds)

    if len(player_one.all_cards)==0:
        print('Player one lost')
        game_on=False
        break
    if len(player_two.all_cards)==0:
        print('Player two lost')
        game_on=False
        break
    
    player_one_cards=[]
    player_one_cards.append(player_one.remove())

    player_two_cards=[]
    player_two_cards.append(player_two.remove())

    game_start=True
    while game_start:
        if player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            game_start=False

        elif player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            game_start=False

        else:
            print("WAR")
            if len(player_one.all_cards) < 5:
                print('player one lost')
                game_on=False
                break
            elif len(player_two.all_cards) < 5:
                print('player two lost')
                game_on=False
                break
            else:
                for i in range(5):
                    player_one_cards.append(player_one.remove())
                    player_two_cards.append(player_two.remove())


        
