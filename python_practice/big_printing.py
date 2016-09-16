#!/usr/bin/env python
"""
__author__ = , 7/11/16
"""

import os
import sys
from os import path
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import init

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected


# cprint(figlet_format('error!', font='starwars'), 'yellow', 'on_red', attrs=['bold'])


class BigPrint:

    def __init__(self, fg_color, bg_color, style='bold', font='starwars', **kwargs):

        self.fg_color = fg_color
        self.bg_color = bg_color
        self.style = style
        self.font = font

    def print_big(self, msg):

        cprint(figlet_format(msg.capitalize(), self.font), self.fg_color, self.bg_color, attrs=[self.style])

    def set_font(self, font_name):

        self.font = font_name

    def __dict__(self):

        return {'fg_color'  : self.fg_color
                , 'bg_color': self.bg_color
                , 'style'   : self.style
                , 'font'    : self.font
                }

printer = BigPrint('yellow', 'on_red')
printer.print_big('Welcome to the Farter')

printer.font = 'Times'
printer.print_big('fart')

printer.set_font('starwars')
printer.print_big('fart')

p2 = BigPrint('red', 'on_blue', font='Times')
p2.print_big('PooooooP')
