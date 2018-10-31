#!/usr/bin/python

import argparse
from svglabel import json2svg

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('jsonfile')
    parser.add_argument('-o', '--outfile')
    args = parser.parse_args()

    json2svg(args.jsonfile,
             outfile=args.outfile,
    )
