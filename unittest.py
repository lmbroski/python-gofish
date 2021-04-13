import unittest
from gofish import Deck
from gofish import Player
from gofish import startRound

class TestDeck(unittest.TestCase):
    """Tests for the class Deck."""
    def setUp(self):
        self.deck = Deck()

    def test_full_deck(self):
        # At beginning of the game there should be 52 cards.
        self.assertEqual(self.deck.build_deck, 52)
        # Test inital deck with missing cards.
        deck = Deck(48)
        self.assertEqual(deck.build_deck, 48)
        # Test inital deck with more than 52 cards
        deck = Deck(56)
        self.assertEqual(deck.build_deck, 56)

    def test_empty_deck(self):
        # When all the cards have been played/are in play.
        deck = Deck(0)
        self.assertEqual(self.deck.deal_top_card, 0)


class TestPlayer(unittest.TestCase):
    """Tests for the class Player."""
    def setUp(self):
        self.hand = Player()

    def test_four_of_a_kind(self):
        # Test whether you completing a suit for one value.
        self.hand.book_check(4)
        self.assertEqual(self.hand.book_check, 4)

     def test_empty_hand(self):
        # Test whether you ran out of cards.
        self.hand.empty_check(0)
        self.assertEqual(self.hand.empty_check, 0)

class TeststartRound(unittest.TestCase):
    """Tests for the class startRound."""
    def setUp(self):
        self.player = startRound()

    def test_taking_turns(self):
        # Test whether you completing a suit for one value.
        self.player.play(4)
        self.assertEqual(self.player[1].play)


unittest.main()
