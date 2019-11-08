#------------Deck of Cards Exercise--------------#
# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should display the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)
from random import shuffle

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

# c1 = Card("A", "Hearts")
# c2 = Card("10", "Diamonds")
# c3 = Card("K", "Spades")
# print(c1,c2,c3)



# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should display information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck.
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck.

		
class Deck:
	def __init__(self):
		suits = ["Hearts","Spades","Diamonds","Clubs"]
		values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
		self.cards = [Card(suit, val) for suit in suits for val in values]

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)

	def _deal(self, number):
		cards_in_deck = self.count()
		to_remove = min(cards_in_deck, number)
		if cards_in_deck == 0:
			raise ValueError("All cards have been dealt!")
		cards_removed = self.cards[-to_remove:]
		self.cards = self.cards[:-to_remove]
		return cards_removed

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled!")
		shuffle(self.cards)
		return self

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size)

deck1 = Deck()
# print(deck1)			#Deck of 52 cards
# print(deck1._deal(2))	#[Q of Clubs, K of Clubs]
# print(deck1)			#Deck of 50 cards
# print(deck1._deal(51))	#[A of Hearts, 2 of Hearts.....]
# print(deck1)			#Deck of 0 cards
# print(deck1._deal(1))	#ValueError: All cards have been dealt!
deck1.shuffle()
card1 = deck1.deal_card()
print(card1)
hand1 = deck1.deal_hand(5)
print(hand1)