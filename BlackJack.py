#!/usr/bin/env python
"""
__author__ = , 9/11/16
"""

import random


class Game:

    CHOICES = []

    def __init__(self):
        self.game_on = False
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deck = Deck()
        self.dealer_score = 0
        self.player_score = 0

    def deal_cards(self):

        if self.game_on:
            self.player_score -= 1

        self.game_on = True
        self.deck = Deck()
        self.deck.shuffle_cards()
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())

        print 'Dealer showing: '
        print self.player_hand

    def hit(self):
        self.player_hand.add_card(self.deck.deal_card())

    def stand(self):
        pass


class Card:

    SUITS = ('D', 'C', 'H', 'S')

    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    VALUES = {

        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10

        }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def __str__(self):
        return 'The {} of {}'.format(self.rank, self.suit)


class Deck:

    SUITS = ('D', 'C', 'H', 'S')

    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self):

        self.cards = []

        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(rank + suit)

    def __str__(self):

        return 'There are {} cards remaining: \n{}'.format(len(self.cards), self.cards)

    def shuffle_cards(self):

        random.shuffle(self.cards)

    def deal_card(self):

        card = self.cards.pop()
        return card


class Hand:

    def __init__(self):

        self.cards = []
        self.total = len(self.cards)

    def __str__(self):

        return '{}'.format(self.cards)

    def add_card(self, card):

        self.cards.append(card)


def main():

    deck = Deck()

    print deck

    deck.shuffle_cards()

    print deck

    hand_one = Hand()

    hand_one.add_card(deck.deal_card())

    dealer_hand = Hand()

    dealer_hand.add_card(deck.deal_card())

    hand_one.add_card(deck.deal_card())

    dealer_hand.add_card(deck.deal_card())

    print deck

    print 'Player has: %s' % hand_one.cards

    print 'Dealer showing: %s' % dealer_hand.cards[0]

    print dealer_hand


if __name__ == '__main__':
    main()