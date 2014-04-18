import argparse
import logging

def parse_args():
	parser = argparse.ArgumentParser(description='App description.')

	parser.add_argument('--verbose', help='Enable verbose output.',action="store_true")
	parser.add_argument('${2}', help='Help for command.')

	args = parser.parse_args()

	if args.verbose:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.INFO)


	if args.${2}:
		return args.${2}
	else:
		parser.print_help()
		return

command = parse_args()

print command
