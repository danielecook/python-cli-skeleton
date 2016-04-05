#! /usr/bin/env python

"""
usage:
	cli <command>
"""

from docopt import docopt

from clint.textui import colored, puts, indent

def main():
    args = docopt(__doc__,
                  options_first=True)
    print(args)


if __name__ == '__main__':
    main()