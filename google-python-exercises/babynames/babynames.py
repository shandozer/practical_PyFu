#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
from os import path
import shutil

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """

    names_file = path.join(filename)

    names_list = []

    try:
        f = open(names_file, 'rU')

        text = f.read()
    except IOError:
        return

    year_pattern = r'in\s\d\d\d\d<'

    year_match = re.search(year_pattern, text)
    print year_match.group().strip('in <')

    if year_match:
        year = year_match.group().strip('in <')
        names_list.append(year)

    name_rank_pat = '<td>([\d]+)</td><td>(\w+)</td><td>(\w+)</td>'

    name_rank_match = re.findall(name_rank_pat, text)

    if name_rank_match:
        ranks = [rank for rank in name_rank_match]

        #print ranks

        names_dict = {}
        for rank in ranks:
            names_dict[rank[0]] = [rank[1], rank[2]]

        #print names_dict

        for k, v in names_dict.items():

            names_list.append(v[0] + ' ' + str(k))
            names_list.append(v[1] + ' ' + str(k))

    #print sorted(names_list)

    return sorted(names_list)


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    for filename in args:

        file_path = path.abspath(filename)

        if path.exists(file_path):

            baby_names = extract_names(filename)

        else:

            print 'file %s does not exist' % filename
            continue

        if summary:

                new_filename = filename.replace('.html', '.summary')
                print new_filename
                g = open(path.join(new_filename), 'wb')

                g.writelines(' \n'.join(baby_names))
                g.close()

        else:
            print baby_names[0]  # year
            for name in baby_names[1:]:
                print name
  
if __name__ == '__main__':
    main()
