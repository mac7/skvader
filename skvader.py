#!/usr/bin/env python

__author__ = 'mac7'

import sys
import utils


def main(argv):
    div = '_' * 32 + '\n'
    output =  utils.pingpong(argv[0])
    for i in [0,6,12]:
        print '%s\nPacket size = %s\nPacket loss = %s\nrtt min = %s ms\nrtt max = %s ms\nrtt avg = %s ms\njitter (avg) = %s ms\n%s\n' % (div, output[i], output[i+1], output[i+2], output[i+3], output[i+4], output[i+5], div)


if __name__ == '__main__':
	try:
		main(sys.argv[1:])
	except:
		print """
		Usage:
		        skvader.py -host """
