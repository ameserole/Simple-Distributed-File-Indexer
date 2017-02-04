"""
Simple Distributed File Indexer
"""

import argparse

word_index = {}	#Dictionary to hold master index of all words encountered

def text_parser(file):
	"""Read in text from file and split into a list of strings.
	   The words will be delimited by anything that is not alphanumeric"""

	text = file.read()
	full_text = ''
	
	for char in text:
		if char.isalnum() or char.isspace():
			full_text += char
		else:
			full_text += ' '	#if the character is not alphanumeric just put a space so that
								#can split it more easily later

	return full_text.split()

def word_indexer(word_list):
	"""Takes in a list of strings and indexes them into the master index"""
	
	for word in word_list:
		if word in word_index:
			word_index[word] += 1
		else:
			word_index[word] = 1



def main():
	"""This function parses the command line arguments and creates a list of files that 
	   will be indexed"""
	#global word_index
	
	parser = argparse.ArgumentParser(description="Simple Distributed File Indexer")
	parser.add_argument('files', metavar='text-file', type=argparse.FileType('r'), nargs='+',
						help="List of text files to be indexed")

	args = parser.parse_args()
	for file in args.files:
		word_list = text_parser(file)
		word_indexer(word_list)

	print(word_index)


if __name__ == '__main__':
	main()