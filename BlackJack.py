#!/usr/bin/env python
"""
__author__ = , 9/11/16
"""

import random
import sys


class Game:

    CHOICES = ['hit', 'stand', 'deal (forfeits current hand)']

    def __init__(self):
        self.game_on = False
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deck = Deck()
        self.dealer_score = 0
        self.player_score = 0
        self.outcome = ""

    def deal_cards(self):

        if self.game_on:
            self.outcome = 'Player forfeited game and started a new one!'
            print self.outcome
            self.player_score -= 1
            self.game_on = False
        else:
            self.deck = Deck()
            self.deck.shuffle_cards()
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

            print 'Dealer showing: {}'.format(self.dealer_hand.cards[0])
            # print 'Player has: {}'.format(self.player_hand.cards)
            print 'Player has: {}, {} \n\tValue is {}'.format(self.player_hand.cards[0], self.player_hand.cards[1],
                                                              self.player_hand.get_value())
            self.game_on = True
            self.outcome = self.player_choice()

    def hit(self):

        if self.game_on:

            if self.player_hand.get_value() <= 21:

                self.player_hand.add_card(self.deck.deal_card())

            print self.player_hand.cards[0:len(self.player_hand.cards)-1]

            if self.player_hand.get_value() > 21:

                self.outcome = "Player Busted!"
                print(self.outcome)

                self.player_score -= 1
                self.game_on = False

            print self.player_hand.get_value()
            self.player_choice()

    def stand(self):

        self.game_on = False

        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())

        print 'Dealer has: {}'.format(self.dealer_hand.get_value())

        if self.dealer_hand.get_value() > 21:
            self.outcome = "\n{}\nDealer Busted! PLAYER WINS!".format(72*'=')
            self.player_score += 1
            print self.outcome
            print "Play Again?"

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

            while choice in Game.CHOICES:
                if choice == 'hit':
                    self.hit()
                elif choice == 'stand':
                    self.stand()
                elif choice == 'deal':
                    self.deal_cards()

            print '\nPlayer has chosen to {}'.format(choice)
            return choice

        except KeyboardInterrupt:
            print '\nExiting...'
            sys.exit()


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
        return self.rank + self.suit


class Deck:

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


class Hand:

    def __init__(self):

        self.cards = []
        self.total = len(self.cards)

    def __str__(self):

        return self.cards[0]

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

    while not g.game_on:

        print "what would you like to do?\nChoices:\t{}".format(" ".join(Game.CHOICES))

        player_choice = raw_input("\n > ")

        if 'hit' in player_choice:
            if g.game_on:
                pass


if __name__ == '__main__':
    main()
