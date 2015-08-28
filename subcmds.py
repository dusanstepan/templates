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

def main_listen (func, threshold, outdir):
    try:
        print 'Listening...'
        
    except KeyboardInterrupt as e:
        print "\nUser interrupt detected."
        raise e

    except IOError as e:
        print str(e)
        traceback.print_exc()
        sys.exit(1)

    except Exception as e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        sys.exit(2)

def main_play(func, outdir):
    try:
        print 'Playing...'
        
    except KeyboardInterrupt as e:
        print "\nUser interrupt detected."
        raise e

    except IOError as e:
        print str(e)
        traceback.print_exc()
        sys.exit(1)

    except Exception as e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        sys.exit(2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(help='Listen or play')
    
    parser_listen = subparsers.add_parser('listen', 
            help='Listen for sounds louder than threshold and record')
    parser_listen.add_argument('threshold', type=float, nargs='?', default=45.0, 
            help="Threshold for sound detection")
    parser_listen.add_argument('-o', '--outdir', help="Output directory",
            default="./recorded_files/")
    parser_listen.set_defaults(func=main_listen)
    
    parser_play = subparsers.add_parser('play', help='Plays recorded files')
    parser_play.add_argument('-o', '--outdir', help="Output directory",
            default="./recorded_files/")
    parser_play.set_defaults(func=main_play)

    args = parser.parse_args()

    args.func(**vars(args))

