#!/usr/bin/env python
"""
__author__ = Shannon Buckley, 9/11/16
"""

import random
import sys
import pygame
from os import path
from pygame.locals import *

VERSION = '1.1.0'


def load_png(name):

    fullname = path.join(path.dirname(sys.argv[0]), name)

    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Unable to load image', fullname
        raise SystemExit, message

    return image, image.get_rect()


class Game(object):

    CHOICES = ['hit', 'stand', 'deal']

    def __init__(self):
        self.game_on = False
        self.player_hand = Hand((25, 200))
        self.dealer_hand = Hand((25, 25))
        self.deck = Deck()
        self.deck.shuffle_cards()
        self.dealer_score = 0
        self.player_score = 0
        self.outcome = ""

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.size = [self.SCREEN_WIDTH, self.SCREEN_HEIGHT]

        # TODO: decide whether / where to implement this section
        # pygame.init()
        # self.screen = pygame.display.set_mode(self.size)
        # self.background = pygame.Surface(screen.get_size())

        # self.all_sprites_list = pygame.sprite.Group()
        #
        # for card in self.player_hand.cards:
        #
        #     self.all_sprites_list.add(card)

    def deal_cards(self):

        self.deck = Deck()
        self.player_hand.empty_hand()
        self.dealer_hand.empty_hand()

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

        if self.game_on:

            if self.player_hand.get_value() <= 21:
                self.player_hand.add_card(self.deck.deal_card())

            self.outcome = 'Player has: {}\n\tValue is {}'.format(self.player_hand,
                                                                  self.player_hand.get_value())
            print(self.outcome)

            if self.player_hand.is_busted():

                self.game_on = False
                self.outcome = "You Busted!"
                print(self.outcome)
                self.player_score -= 1

            self.player_choice()

    def stand(self):

        self.outcome = "\nPlayer chose to stand! Dealer has: {} ({})".format(self.dealer_hand,
                                                                             self.dealer_hand.get_value())

        print self.outcome
        self.game_on = False

        while self.dealer_hand.get_value() < 17:

            next_card = self.deck.deal_card()

            print "\nDealer Must Take a Card: {}!".format(next_card)

            self.dealer_hand.add_card(next_card)

            print "\nDealer's Hand is now: {} ({})".format(self.dealer_hand, self.dealer_hand.get_value())

            print '\nDealer has: {}'.format(self.dealer_hand.get_value())

        if self.dealer_hand.is_busted():

            self.outcome = "\n{}\nDealer Busted! PLAYER WINS!".format(72*'=')
            self.player_score += 1

        else:
            if self.dealer_hand.get_value() >= self.player_hand.get_value() or self.player_hand.is_busted():
                self.outcome = "\n{}\nDealer Wins! :(".format(72 * '=')
                self.player_score -= 1
            elif len(self.player_hand.cards) == 5 and self.player_hand.get_value() <= 21:
                self.outcome = "\n{}\n5 Cards without busting? LUCKY PLAYER Wins!:(".format(72 * '=')
            else:
                self.outcome = "\n{}\nDealer ({}) | Player ({}) --> PLAYER Wins! :)".format(72 * '=',
                                                                                            self.dealer_hand.get_value(),
                                                                                            self.player_hand.get_value())
                self.player_score += 1

        print self.outcome
        self.player_choice()

    def player_choice(self):

        try:
            if not self.game_on:
                choices = Game.CHOICES[-1]
            else:
                choices = Game.CHOICES

            choice = raw_input('What do you do? Choices = {}'.format(choices))

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

    def write(self, info, color=(0, 0, 0), fontsize=24):
        game_font = pygame.font.SysFont("None", fontsize)
        text_to_write = game_font.render(info, True, color)
        text_to_write = text_to_write.convert_alpha()

        return text_to_write

    def draw(self, screen, sprite, x, y):
        screen.blit(sprite, (round(x, 0) - sprite.get_width()/2,
                             round(y, 0) - sprite.get_height()/2))


class Card(pygame.sprite.Sprite):

    SUITS = ('D', 'C', 'H', 'S')

    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    VALUES = {

        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10

        }
    card_images = pygame.image.load('./assets/cards.jfitz.png')

    CARD_SIZE = (73, 98)
    CARD_CENTER = (36.5, 49)

    def __init__(self, rank, suit):
        pygame.sprite.Sprite.__init__(self)
        self.rank = rank
        self.suit = suit

        self.image = Card.card_images
        self.rect = self.image.get_rect()

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

    def __init__(self, starting_position):
        self.starting_position = starting_position
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

    def is_busted(self):

        if self.get_value() > 21:
            return True
        else:
            return False

    def empty_hand(self):
        self.cards = []


class SpriteSheet(object):
    """Class used to slice images out of a sprite sheet."""

    def __init__(self, filename):

        self.filename = filename

        try:
            self.sprite_sheet = pygame.image.load(path.join(path.dirname(sys.argv[0]), self.filename))
            self.sprite_sheet = self.sprite_sheet.convert_alpha()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', self.filename
            raise SystemExit, message

    # get specific image from specific rectangular region (x,y)
    def get_image(self, x, y, width, height, colorkey=None):

        rectangle = (x, y, width, height)

        rect = pygame.Rect(rectangle)

        # make new blank img
        image = pygame.Surface(rect.size).convert_alpha(rect)

        image.blit(self.sprite_sheet, (0, 0), rect)

        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            else:
                colorkey = (0, 0, 0)  # black
            image.set_colorkey(colorkey, pygame.RLEACCEL)

        return image


def main():

    g = Game()

    g.deal_cards()

    SIZE = [800, 600]

    bg_color = (0, 255, 0)

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("BlackJack with sprite sheet...")

    # fill BG
    screen.fill(bg_color)

    running = True

    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    else:
        print 'game over!'

        pygame.display.flip()

if __name__ == '__main__':
    main()
