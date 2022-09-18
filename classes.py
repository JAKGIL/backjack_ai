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
    