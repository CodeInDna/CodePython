from random import shuffle
from cards import Card
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