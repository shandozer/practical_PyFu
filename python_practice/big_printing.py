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


cprint(figlet_format('error!', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
