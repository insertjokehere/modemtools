#!/usr/bin/env python

import modemtools

import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--url', action='store', help='Base URL of device')
	parser.add_argument('--username', default=None, help='Username to send to the device')
	parser.add_argument('--password', default=None, help='Password to send to the device')
	subparsers = parser.add_subparsers(help='sub-command help')
	
	# create the parser for the "a" command
	parser_listdevices = subparsers.add_parser('list-devices', help='Lists supported devices')
	parser_listdevices.set_defaults(func=listDevices)

	args = parser.parse_args()
	args.func(args)

def listDevices(args):
	print dir(modemtools)
	detector = modemtools.detect.deviceDetector("http://example.com")
	print detector.getAllDevices()

if __name__ == "__main__":
	main()