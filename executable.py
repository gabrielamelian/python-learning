#!/usr/bin/env python

"""
Test program executable file
"""

import argparse

parser = argparse.ArgumentParser(description='Requires a name')

parser.add_argument('-n', '--name')
arguments = parser.parse_args()

print "Hello %s" % arguments.name
