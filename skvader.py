#!/usr/bin/env python

__author__ = 'mac7'

import sys
import utils


def main(argv):
	div = '_' * 32 + '\n'
	print '%s\nPacket loss = %s\nrtt min = %s ms\nrtt avg = %s ms\nrtt max = %s ms\njitter (avg) = %s ms\n%s' % (div,
																									 utils.pingpong(argv[0])[0],
																									 utils.pingpong(argv[0])[1],
																									 utils.pingpong(argv[0])[2],
																									 utils.pingpong(argv[0])[3],
																									 utils.pingpong(argv[0])[4],
																									 div)


if __name__ == '__main__':
	try:
		main(sys.argv[1:])
	except:
		print """
		Usage:   
                skvader.py -host
"""
