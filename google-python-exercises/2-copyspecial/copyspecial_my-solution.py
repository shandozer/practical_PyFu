#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""
The Copy Special exercise goes with the file-system and external commands material in the Python Utilities section.
This exercise is in the "copyspecial" directory within google-python-exercises (download google-python-exercises.zip
if you have not already, see Set Up for details). Add your code in copyspecial.py.

The copyspecial.py program takes one or more directories as its arguments.

We'll say that a "special" file is one where the name contains the pattern __w__ somewhere, where the w is one or more
word chars. The provided main() includes code to parse the command line arguments, but the rest is up to you.
Write functions to implement the features below and modify main() to call your functions.
"""

# +++your code here+++
# Write functions and modify main() to call them


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    # +++your code here+++
    # Call your functions
  
if __name__ == "__main__":
    main()
