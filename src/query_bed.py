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
    
    tabel = Table()

    for line in args.bed:
        tabel.add_line(parse_line(line))

    for line in args.query:
        chrom, start, end = line.split()
        overlaps = tabel.get_chrom(chrom)
        if len(overlaps) > 0:
            for i in overlaps:
                if int(start) <= i[1] and i[2] <= int(end):
                    print_line(i, args.outfile)

        

if __name__ == '__main__':
    main()
