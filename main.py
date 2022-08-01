from hashlib import new
from operator import truediv
from os import remove
import random
from time import sleep

class Deck:
    def __init__(self):
        self.cards = []

        for i in range(10): #Regular numbers
            for j in range(4):
                self.cards.append(i)
        for i in range(4):
            self.cards.remove(0)
            
        for i in range(12): #Kings, Queens and Jack's 
            self.cards.append(10)
    
        for i in range(4): #Ases
            self.cards.append(11)

    def draw_a_card(self):
        selected_card = self.cards[random.randint(0,len(self.cards)-1)]
        self.cards.remove(selected_card)
        return selected_card

class Hand:
    def __init__(self, deck):
        self.cards =[deck.draw_a_card(), deck.draw_a_card()]

    def draw(self, deck):
        self.cards.append(deck.draw_a_card())
    
    def sum_up(self):
        sum = 0
        for i in self.cards:
            sum = sum + i
        return sum
    
def show_stats(player_hand, croupier_hand):
    print("-------------------------")        
    print("------Croupier hand------")
    print(["?",croupier_hand.cards[1]])
    print("Sum:{}".format(croupier_hand.cards[1]))
    
    print("--------Your hand-------")
    print(player_hand.cards)
    print("Sum:{}".format(player_hand.sum_up()))


def main():
    #Setting up hands
    new_deck = Deck()
    croupier_hand = Hand(new_deck)
    player_hand = Hand(new_deck)

    #Main game
    stays = False
    while stays == False:
        show_stats(player_hand=player_hand, croupier_hand=croupier_hand)
        
        imp = input("Press \"D\" to draw or \"S\" to stay:")
        if imp == "D" :
            player_hand.draw(new_deck)
        if imp == "S":
            stays = True

    

    while croupier_hand.sum_up() <= player_hand.sum_up():
        show_stats(player_hand=player_hand, croupier_hand=croupier_hand)

        croupier_hand.draw(new_deck)
        sleep(2)
    
    print("------Croupier hand------")
    print(croupier_hand.cards)
    print("Sum:{}".format(croupier_hand.sum_up()))

    print("--------Your hand-------")
    print(player_hand.cards)
    print("Sum:{}".format(player_hand.sum_up()))     
        
main()