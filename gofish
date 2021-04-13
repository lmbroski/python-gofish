import random
import sys
import os
from collections import defaultdict
from collections import Counter

class Cards(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # built in methods for printing the card object 
    def __unicode__(self):
        return self.faces()
    def __str__(self): # readability
        return self.faces()
    def __repr__(self): # unambigious
        return self.faces()

    card_value = ['2', '3', '4','5', '6', '7', '8', '9',  'Jack', 'Queen', 'King', 'Ace']
    card_suit = ['Clubs ♣ ', 'Diamonds ♦ ', 'Hearts ♥ ', 'Spades ♠']

    DECK = (card_value *4)

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value 

    def get_suit(self): 
        return self.suit[self.card_suit]

    def get_value(self):
        return self.value [self.card_value]
    
    def faces(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)

class Deck(object): 
    
    def __init__(self):
        self.cards = []
        self.build_deck()

    def whole_deck(self):
        for card in self.cards:
            print(card.show())

    # Generates 52 cards
    def build_deck(self):   
        self.cards = []
        for card_suit in ['Hearts ♥', 'Clubs ♣', 'Diamonds ♦', 'Spades ♠']:
            for card_value in range(1, 14):
                self.cards.append(Cards(card_suit, card_value))

    def shuffle_deck(self, num=1):
        length = len(self.cards)
        # This is the "fisher yates shuffle algorithm"
        for _ in range(num):
            for i in range(length-1, 0, -1):
                rnd = random.randint(0, i)
                if i == rnd:
                    continue
                self.cards[i], self.cards[rnd] = self.cards[rnd], self.cards[i]

    def deal_top_card(self):
        if len(self.cards) == 0:
            return "Deck is empty"
        else:
            return self.cards.pop()

class Player(object):
    def __init__(self, deck):
        self.book = []
        self.deck = deck 
        self.hand = []
        self.name = input("Enter your name: ")
        self.score = 0

    # Removes card from the deck, adds the card to players hand
    def draw(self, deck, num=1):
        c_drawn = self.deck.pop()
        self.hand[c_drawn] += 1 
        print('%s drew %s.' % (self.name,c_drawn))
        self.checkForBooks()

    def book_check(self):
        for key,val in self.hand.items():
            if val == 4: 
                self.book.append(key)
                print('%s completed the book of %s\'s.' % (self.name,key))
                self.score += 1
                del self.hand[key]
            else:
                raise Exception("Book is not found")
            return self.emptyCheck()

    def empty_check(self):
        if len(self.deck)!=0 and len(self.hand)==0:
            self.draw(card)

    def my_hand(self):
        print("{}'s hand: {}".format(self.name, self.hand))
        return self

    def p_turn(self):
        c_pick = input('What card do you ask for?')
        if c_pick not in self.hand:
            print('Unavailable Card. Please re-try.')
            c_pick = self.take_turn()
        return c_pick

    # if the card is available, returns the count and removes card from hand
    def p_fishing(self,card):
        if card in self.hand: 
            val = self.hand.pop(card)
            self.emptyCheck()
            return val
        else:
            raise Exception("Sorry, the other player did not have that card")
            return False
            
    def p_card_check(self,card,amount):
        self.hand[card] += amount
        self.checkForBooks()
    
class Opponent(Player):
    def __init__(self,deck):
        self.name = 'Computer'
        self.hand = []
        self.book = []
        self.deck = deck
        self.score = 0

    def draw(self,deck, num=1): 
        c_drawn = self.deck.pop()
        self.hand[c_drawn] += 1 
        self.book_check()

    def c_turn(self):
        print(self.my_hand())
        player = list(self.hand.keys())
        if not player:
            player = self.hand.keys() 
        return move

    def c_fishing(self,card):
        self.name.add(card)
        if card in self.hand: 
            val = self.hand.pop(card)
            self.empty_check()
            return val
        else:
            raise Excpetion("Sorry, the other player did not have that card")
            #return False

    def c_card_check(self,card,amount):
        self.hand[card] += amount
        self.name.discard(card)
        self.book_check()

class startRound(object):
    def __init__(self):
        self.deck = ('')
        self.player = [Player(self.deck), Opponent(self.deck)]

    def play(self):
        random.shuffle(self.deck)
        for i in range(7): # Deal the first cards
            self.player[1].draw(self.deck)
            self.player[2].draw(self.deck)

        turn = 1
        def in_hand(self, p_hand, c_hand, i_guess, whole_deck, deck, current_player, c_guess):
        indices = [i for i, x in enumerate(c_hand) if x.card_number == guess]
        
        # Draw card if guess doesn't match
        if not indices:
            print('Go Fish!')
            p_hand, whole_deck = deck.draw_cards(whole_deck, p_hand, 2)
            c_guess = False
        # Removing from a hand if matched
        else:
            print('You guessed it!')
            for index in sorted(indices, reverse=True):
                p_hand.append(c_hand.pop(index))                            
                c_guess = True

        return p_hand, c_hand, whole_deck, c_guess

    #def scoring_cycle(self, p_hand, player_pts):
    #    counts = Counter(p_hand)
    #    match = False
    #    for book in counts:
    #        if (counts[book] == 4):
    #           print("There is four of a kind:")
    #            print(book)
    #            p_hand.remove(book)                
    #            print(player_name + str(player_pts))
    #           match = True
    #    if match:
    #        player_pts += 1
            
    #    return p_hand, player_pts
    
    # key=lamda anonymous functions for sorting
    def print_p_hand(self,p_hand)
        p_hand.sort(key=lambda x: x.card_number) 
        print(p_hand)
    
    def print_c_hand(self,c_hand)
        c_hand.sort(key=lambda x: x.card_number) 
        print(c_hand)

    def ending_cycle(self):
        input("Press enter when ready...")
        input("Please pass the game to the next player...")

if __name__=="__main__":
    game = startRound()
    game.play()


