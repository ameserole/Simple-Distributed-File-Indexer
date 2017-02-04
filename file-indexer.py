"""
Simple Distributed File Indexer
"""

import argparse



def main():
	"""This function parses the command line arguments and creates a list of text files that 
	   will be indexed"""
	
	parser = argparse.ArgumentParser(description="Simple Distributed File Indexer")
	parser.add_argument('files', metavar='text-file', type=argparse.FileType('r'), nargs='+',
						help="List of text files to be indexed")

	args = parser.parse_args()
	for x in args.files:
		print(x.read())

if __name__ == '__main__':
	main()