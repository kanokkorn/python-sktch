import random
import time

class card(object):
  def __init__(self, suit, val):
    self.suit = suit
    self.val = val

  def show(self):
    print('%s of %s'%(self.val, self.suit))

class deck(object):
  def __init__(self):
    self.cards = []
    self.build()
  
  def build(self):
    for _ in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
      for x in range(1, 14):
        self.cards.append(card(_, x))
  
  def show(self):
    for s in self.cards:
      s.show()

  def shuffle(self):
    for a in range(len(self.cards)-1, 0, -1):
     rand = random.randint(0, a)
     self.cards[a], self.cards[rand] = self.cards[rand], self.cards[a]
  
  def drawCard(self):
    return self.cards.pop()

class player(object):
  def __init__(self):
    self.hand = []

  def draw(self, deck):
    self.hand.append(deck.drawCard())

  def showHand(self):
    for card in self.hand:
      card.show()
  
  def discard(self):
    self.hand.pop()

if __name__ == "__main__":
  deck = deck()
  deck.shuffle()