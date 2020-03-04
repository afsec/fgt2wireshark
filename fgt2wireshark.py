#!/usr/bin/env python
# Author: Antonio Feitosa
# source: https://github.com/afsec/fgt2wireshark

import argparse
import re
import os

regex = "^0x(\d+)\W+(\w\w)(\w\w)\W?(\w\w)?(\w\w)?\W?(\w\w)?(\w\w)?\W?(\w\w)?(\w\w)?\W?(\w\w)?(\w\w)?\W?(\w\w)?(\w\w)?\W?(\w\w)?(\w\w)?\W?(\w\w)?(\w\w)?"

def is_valid_file(parser, arg):
    """

    :rtype : open file handle
    """
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')

parser = argparse.ArgumentParser(description='Convert Fortigate dump to Wireshark HexDump.')
parser.add_argument("-i", dest="filename", required=True,
                    help="""input file with output of FGT command "diagnose sniffer packet <iface> none 6" """, metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))

args = parser.parse_args()

for line in args.filename.readlines():
    if re.match("^0x0000",line):
        print("")
    matches = re.findall(regex, line)
    if matches:
        for line in matches:
            print(' '.join(line))
