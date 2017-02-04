"""
Simple Distributed File Indexer
Andrew Meserole
"""

import argparse

word_index = {}	#Dictionary to hold master index of all words encountered

def text_parser(file):
	"""Read in text from file and split into a list of words delimited by anything that is not alphanumeric
	   Input: file to be tokenized
	   Output: list of everyword found"""

	text = file.read()
	full_text = ''
	
	for char in text:
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
	for i in range(10):
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

def main():
	"""Parse the command line arguments, indexes the list of words in a file, and prints the top ten words"""
	
	parser = argparse.ArgumentParser(description="Simple Distributed File Indexer")
	parser.add_argument('files', metavar='text-file', type=argparse.FileType('r'), nargs='+',
						help="List of text files to be indexed")

	args = parser.parse_args()
	word_list = []
	
	for file in args.files:
		word_list += text_parser(file)
	
	print_sorted(word_indexer(word_list))


if __name__ == '__main__':
	main()