#!/usr/bin/env python

__author__ = 'mac7'

import sys
import utils


def main(argv):
	div = '#'*76
	print '%s\n%s\n%s' % (div, utils.pingpong(argv[0]).rstrip(), div)



if __name__ == '__main__':
	try:
	    	main(sys.argv[1:])
	except:
		print """
		Usage:   
                skvader.py -host
"""
