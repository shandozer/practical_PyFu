#!/usr/bin/env python
"""
__author__ = Shannon Buckley, 9/11/16
__version__ = 1.0.0
"""

import random
import sys


class Game(object):

    CHOICES = ['hit', 'stand', 'deal']

    def __init__(self):
        self.game_on = False
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deck = Deck()
        self.deck.shuffle_cards()
        self.dealer_score = 0
        self.player_score = 0
        self.outcome = ""

    def deal_cards(self):

        self.__init__()  # dump any cards they have, re-deal
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())

        self.game_on = True

        print 'Dealer showing: {}'.format(self.dealer_hand.cards[0])

        print 'Player has: {} \n\tValue is {}'.format(self.player_hand,
                                                      self.player_hand.get_value())

        if self.player_hand.check_blackjack():
            self.outcome = "\nPlayer has BlackJack! PLAYER WINS! "
        elif self.dealer_hand.check_blackjack():
            self.outcome = "\nDealer has BlackJack! DEALER WINS :("

        self.outcome = self.player_choice()

    def hit(self):

        if not self.game_on:
            self.player_choice()

        if self.game_on:

            if self.player_hand.get_value() <= 21:

                self.player_hand.add_card(self.deck.deal_card())

                self.outcome = 'Player has: {}\n\tValue is {}'.format(self.player_hand,
                                                                      self.player_hand.get_value())
                print(self.outcome)

                self.player_choice()

            print self.player_hand.cards[0:len(self.player_hand.cards)-1]

            if self.player_hand.get_value() > 21:

                self.outcome = "Player Busted!"
                print(self.outcome)

                self.player_score -= 1
                self.game_on = False

            print self.player_hand.get_value()

    def stand(self):

        self.game_on = False

        print "\nPlayer chose to stand! Dealer has: {}".format(self.dealer_hand)

        while self.dealer_hand.get_value() < 17:

            next_card = self.deck.deal_card()

            print "\nDealer Must Take a Card: {}!".format(next_card)

            self.dealer_hand.add_card(next_card)

            print "\nDealer's Hand is now: {}".format(self.dealer_hand)

            print '\nDealer has: {}'.format(self.dealer_hand.get_value())

        if self.dealer_hand.get_value() > 21:

            self.outcome = "\n{}\nDealer Busted! PLAYER WINS!".format(72*'=')
            self.player_score += 1

            print self.outcome
            print "Play Again?"

        elif self.player_hand.get_value() > 21:

            self.outcome = "\n{}\nPlayer has Busted! DEALER WINS :( ".format(72*'=')
            self.dealer_score += 1

        else:
            if self.dealer_hand.get_value() >= self.player_hand.get_value() or self.player_hand.get_value() > 21:
                self.outcome = "Dealer Wins! :("
                self.player_score -= 1

            else:
                self.outcome = "Player wins!"
                self.player_score += 1

        print self.outcome
        self.player_choice()

    def player_choice(self):

        try:

            choice = raw_input('What do you do? Choices = {}'.format(Game.CHOICES))

            while True:
                if choice == 'hit':
                    self.hit()
                elif choice == 'stand':
                    self.stand()
                elif choice == 'deal':
                    self.deal_cards()
                else:
                    self.player_choice()

            print '\nPlayer has chosen to {}'.format(choice)
            return choice

        except KeyboardInterrupt:
            print '\nExiting...'
            sys.exit()


class Card(object):

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
        return self.rank + self.suit


class Deck(object):

    SUITS = ('D', 'C', 'H', 'S')

    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self):

        self.cards = []

        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(rank, suit))

    def __str__(self):

        return 'There are {} cards remaining: \n{}'.format(len(self.cards), self.cards)

    def shuffle_cards(self):

        random.shuffle(self.cards)

    def deal_card(self):

        card = self.cards.pop()

        return card


class Hand(object):

    def __init__(self):

        self.cards = []
        self.total = len(self.cards)

    def __str__(self):

        hand = ''
        for card in self.cards:
            hand += ' ' + card.__str__()

        return hand

    def add_card(self, card):

        self.cards.append(card)

    def get_value(self):

        hand_value = 0

        has_ace = False

        for card in self.cards:

            rank = card.get_rank()

            hand_value += Card.VALUES[rank]

            if rank == 'A':

                has_ace = True

        if hand_value < 11 and has_ace:
            hand_value += 10

        return hand_value

    def check_blackjack(self):

        if 'A' in self.cards:
            if '10' or 'J' or 'Q' or 'K' in self.cards:

                print '\nBlackJack!'


def main():

    g = Game()

    g.deal_cards()


if __name__ == '__main__':
    main()
