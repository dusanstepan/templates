#!/usr/bin/env python
"""

DESCRIPTION

    TODO This describes how to use this script. This docstring
    will be printed by the script if there is an error or
    if the user requests help (-h or --help).

EXAMPLES

    TODO: Show some examples of how to use this script.

EXIT STATUS

    TODO: List exit codes

AUTHOR

    TODO: Name <name@example.org>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.
"""

import argparse
import sys, os, traceback
#import time
#import re
#import numpy as np
#import matplotlib.pyplot as plt

def main (infile, outfile = None):

    print 'Hello world!'

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description=__doc__,
                formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('infile', help="Input file",
                type=str)
#                type=argparse.FileType('r'))
        parser.add_argument('-o', '--outfile', help="Output file",
                default=sys.stdout, type=argparse.FileType('w'))
        args = parser.parse_args()

        main(**vars(args))

        sys.exit(0)

    except KeyboardInterrupt, e: # Ctrl-C
        raise e

    except SystemExit, e: # sys.exit()
        raise e

    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)

