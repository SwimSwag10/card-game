from classes.deck import Deck
import random

bicycle = Deck()

class Player:
    def __init__(self, name):
      self.name = name
      self.hand = []

    def ask_user():
      player1 = Player("Player 1")
      player2 = Player("Player 2")
      ask = input("Do you want to play cards? ").upper()
      if ask == "YES" or ask == "Y":
        player1.draw(bicycle)
        player2.draw(bicycle)
        player1.show_hand()
        player2.show_hand()
        if player1.hand[0].point_val > player2.hand[0].point_val:
          print(f"{player1.name} wins!")
        else:
          print(f"{player2.name} wins!")
      elif ask == "NO" or ask == "N":
        print("Okay, just run the file again to play!")
      else:
        print("I don't understand, try again.")

    def draw(self, deck):
        self.hand.append(deck.cards.pop(random.randint(0, len(deck.cards) - 1)))

    def show_hand(self):
        for card in self.hand:
            card.card_info()

Player.ask_user()