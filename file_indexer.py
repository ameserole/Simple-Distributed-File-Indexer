"""
Simple Distributed File Indexer
Andrew Meserole

Command-line indexer application that finds the top 10 words across a collection of documents

usage: file_indexer.py [-h] [-f text-file [text-file ...] | -t text-blob
                       [text-blob ...]]

Simple Distributed File Indexer

arguments:
  -h, --help            show this help message and exit
  -f text-file [text-file ...], --files text-file [text-file ...]
                        List of text files to be indexed
  -t text-blob [text-blob ...], --text text-blob [text-blob ...]
                        Blob of text to be indexed
"""

#TODO: Possibly add functionality to remove all common grammar words such as and, is, the, etc.
#TODO: Possibly add functionality to find the longest substring between two or more inputs 
#TODO: Allow file to have stdout from other programs be piped into this one
# 	   Ex) find / | python file_indexer.py -t 
#	   Would output the top ten most common words found from the command 'find /'

import argparse
import sys



word_index = {}	#Dictionary to hold master index of all words encountered

def text_parser(text_blob):
	"""Read in text from a text blob and split into a list of words delimited by anything that is not alphanumeric
	   Input: text blob to be tokenized
	   Output: list of every word found"""
	full_text = ''
	
	for char in text_blob:
		if char.isalnum() or char.isspace():
			full_text += char
		else:
			full_text += ' '	#if the character is not alphanumeric just put a space so that the text
								#can split it more easily later

	return full_text.split()

def word_indexer(word_list):
	"""Takes in a list of words and indexes them into the master index
	   Input: list of words to be indexed in the master index
	   Output: Dictionary with the top ten words in the master index"""
	
	for word in word_list:
		word = word.lower()
		if word in word_index:
			word_index[word] += 1
		else:
			word_index[word] = 1

	sorted_list = sorted(word_index, key=word_index.__getitem__, reverse=True)

	top_ten = {}
	top_length = 10
	
	#If we don't have 10 words to work with only print out how many we have
	if len(sorted_list) < 10:
		top_length = len(sorted_list)

	for i in range(top_length):
		temp_word = word_index.get(sorted_list[i])
		
		#Make sure to not add None to the dictionary if there not actually ten words in the list
		if temp_word != None:	
			top_ten[sorted_list[i]] = temp_word
	
	return top_ten

def print_sorted(word_dict):
	"""Prints out the sorted list of words in the dictionary of words passed to it
	   Input: Dictionary to be sorted and printed"""
	
	sorted_list = sorted(word_dict, key=word_dict.__getitem__, reverse=True)
	
	padding = len(max(sorted_list, key=len)) + 3	#padded spaces to be added after each word to make the printing pretty

	print("Top ten indexed words:")
	i = 1
	for word in sorted_list:
		print("{0:2}. Word: {1:{padding}} Count: {2}".format(i, word, word_dict.get(word), padding=padding))
		i += 1

def clear_master_index():
	"""This clears the global dictionary word_index for unit testing purposes"""
	word_index.clear()

def argument_parser(args_list):
	"""This function parses the arguments passed through the commandline and runs through the rest of the program.
	   Put in a seperate function in order to add unit tests
	   Input: arguments passed through the commandline
	   Output: Prints"""

	parser = argparse.ArgumentParser(description="Simple Distributed File Indexer")
	
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-f','--files', metavar='text-file', type=argparse.FileType('r'), nargs='+',
						help="List of text files to be indexed")

	group.add_argument('-t','--text', metavar='text-blob', type=str, nargs='+', 
						help="Blob of text to be indexed")
	
	args = parser.parse_args(args_list)

	word_list = []
	
	#Check whether a file or a blob of text was passed as an argument and then parse the input
	if args.files is not None:
		for arg in args.files:
			word_list += text_parser(arg.read())
	elif args.text is not None:
		for arg in args.text:
			word_list += text_parser(arg)
	else:
		parser.print_help()
		exit(1)

	sorted_list = word_indexer(word_list)
	print_sorted(sorted_list)
	
	#Done to make testing argparse easier
	return sorted_list


def main():
	"""Parse the command line arguments, indexes the list of words in a file, and prints the top ten words"""
	
	argument_parser(sys.argv[1:])


if __name__ == '__main__':
	main()
