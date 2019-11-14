#Unit Testing (34_oop_deck_of_cards)
from cards import Card
from deck import Deck
import unittest

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card("Hearts", "A")

	def test_init(self):
		self.assertEqual(self.card.suit, "Hearts")
		self.assertEqual(self.card.value, "A")

	def test_repr(self):
		self.assertEqual(repr(self.card), "A of Hearts")

class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		self.assertTrue(isinstance(self.deck.cards, list))
		self.assertEqual(len(self.deck.cards), 52)

	def test_repr(self):
		self.assertEqual(repr(self.deck), "Deck of 52 cards")

	def test_count(self):
		self.assertEqual(self.deck.count(), 52)
		self.deck.cards.pop()
		self.assertEqual(self.deck.count(), 51)

	def test_deal_sufficient_cards(self):
		cards = self.deck._deal(100)
		self.assertEqual(len(cards), 52)
		self.assertEqual(self.deck.count(), 0)

if __name__=='__main__':
	unittest.main()