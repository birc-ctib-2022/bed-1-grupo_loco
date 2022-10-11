"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    parse_line, print_line
)
from query import Table


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',  # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    # FIXME: put your code here
    
    bed = Table

    for y in args.bed:
        bed.add_line(parse_line(y)) # here we add a line from a bed file, and parse the row, such that we have the different elements

    for y in args.query:
        chromosome = bed.get_chrom(y) # getting the chromosome such that i can check for overlap
        chrom, start, end, name = y.split()
        for j in chromosome:
            if int(start) != chromosome[1] or chromosome[2] != int(end):
                print None
            else:
                print_line(j, args.outfile)

if __name__ == '__main__':
    main()
