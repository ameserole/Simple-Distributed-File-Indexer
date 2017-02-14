import unittest
from file_indexer import *

class test_text_parser(unittest.TestCase):
	def setUp(self):
		self.sentence_list = ['This', 'is', 'a', 'sentence']
		self.alphanum_list = ['This','is','a','sentence','with','a','lot','of','special','characters','hello','how','are','you',
							  'First','shalt','thou','take','out','the','Holy','Pin','Then','shalt','thou','count','to','three','no',
							  'more','no','less','Three','shall','be','the','number','thou','shalt','count','and','the','number','of',
							  'the','counting','shall','be','three']
		self.number_list = ['1111','22', '3333', 'number', '4', 'l33t']

	def test_space_delimit(self):
		#Test parser on normal sentence
		file = open('test-files/sentence.txt', 'r')
		text = file.read()
		result = text_parser(text)
		self.assertEqual(result, self.sentence_list, "text_parser tokenized the words in sentence.txt wrong")

	def test_non_alphanum_delimit(self):
		#Test parser on text with several special characters
		file = open('test-files/non-alpha-num.txt', 'r')
		text = file.read()
		result = text_parser(text)
		self.assertEqual(result, self.alphanum_list, "text_parser tokenized the words in non-alpha-num.txt wrong")

	def test_numbers(self):
		#Test parser on a sentence with numbers in it
		file = open('test-files/number-test.txt', 'r')
		text = file.read()
		result = text_parser(text)
		self.assertEqual(result, self.number_list, "text_parser tokenized the words in number-test.txt wrong")

class test_word_indexer(unittest.TestCase):
	def setUp(self):
		self.word_list = ['one','two','two','three','three','three','four','four','four','four','five','five','five','five','five',
						  'six', 'six', 'six', 'six', 'six', 'six', 'seven', 'seven', 'seven', 'seven', 'seven', 'seven', 'seven',
						  'eight','eight','eight','eight','eight','eight','eight','eight','nine','nine','nine','nine','nine','nine',
						  'nine','nine','nine','ten','ten','ten','ten','ten','ten','ten','ten','ten','ten', 'eleven', 'eleven', 'eleven', 
						  'eleven', 'eleven', 'eleven', 'eleven', 'eleven', 'eleven', 'eleven', 'eleven']
		
		self.word_list_mixed_case = ['One','two','twO','three','Three','Three','four','four','FOUR','four','five','five','five','five','five',
						  			 'six', 'six', 'six', 'six', 'six', 'siX', 'seven', 'seven', 'seven', 'seven', 'seven', 'seven', 'seven',
						  			 'eight','eight','EIGHT','eIght','eiGht','eight','eight','eight','nine','nine','nine','nine','nIne','nine',
						  			 'nine','nine','ninE','ten','ten','TEN','ten','ten','ten','ten','ten','ten','ten', 'eleven', 'eleven', 'eleven', 
						  			 'eleven', 'eleven', 'eleven', 'eleven', 'ELEVEN', 'eleven', 'eleven', 'eleveN']

		self.proper_dict = {'eleven':11, 'ten':10, 'nine':9, 'eight':8, 'seven':7, 'six':6, 'five':5, 'four':4, 'three':3, 'two':2}

		#Counts gotten from here: http://www.writewords.org.uk/word_count.asp
		#NOTE: For onliberty.txt http://www.writewords.org.uk/word_count.asp lists "is" as having a count at 1013 but counts "is'" as a seperate word with a count of 1
		self.proper_dict_onliberty = {'the':3488, 'of':2788, 'to':1969, 'and':1478, 'in':1141, 'is':1014, 'a':1008, 'it':856, 'be':768, 'that':740}
	

	def test_word_list(self):
		#Test word indexer on a list of all lower case words
		result = word_indexer(self.word_list)
		self.assertDictEqual(result, self.proper_dict, "word_indexer did not properly index the words")
		clear_master_index()	#Clear the master index in file_indexer.py so that the results of using word_indexer in each test arent felt in others

	def test_word_list_mixed_case(self):
		#Test word indexer on a list of mixed case words
		result = word_indexer(self.word_list_mixed_case)
		self.assertDictEqual(result, self.proper_dict, "word_indexer did not properly index the words with mixed cases")
		clear_master_index()	#Clear the master index in file_indexer.py so that the results of using word_indexer in each test arent felt in others

	def test_large_text(self):
		#Test word indexer on a larger text file
		file = open('test-files/onliberty.txt', 'r')
		text_blob = file.read()
		text = text_parser(text_blob)
		result = word_indexer(text)
		self.assertDictEqual(result, self.proper_dict_onliberty, "word indexer failed to index the words in onliberty.txt")
		clear_master_index()	#Clear the master index in file_indexer.py so that the results of using word_indexer in each test arent felt in others



class test_argparser(unittest.TestCase):
	def setUp(self):
		self.file_arg = ['-f', 'test-files/non-alpha-num.txt']

		self.proper_alpha_dict = {'a': 2, 'be': 2, 'shall': 2, 'thou': 3, 'of': 2, 'no': 2, 'number': 2, 'three': 3, 'the': 4, 'shalt': 3}
		
		#Contains some single and multiword arguments
		self.text_blob_arg = ['-t', 'one two','two','three','three','three','four','four','four','four','five','five','five','five','five',
						  		   'six', 'six', 'six', 'six six six', 'seven', 'seven', 'seven', 'seven', 'seven', 'seven', 'seven',
						  		   'eight','eight','eight','eight','eight','eight','eight','eight nine','nine','nine','nine','nine','nine',
						           'nine','nine','nine','ten','ten','ten','ten','ten','ten','ten','ten','ten','ten', 'eleven', 'eleven', 'eleven', 
						           'eleven', 'eleven', 'eleven', 'eleven', 'eleven', 'eleven', 'eleven', 'eleven']
		
		self.proper_dict = {'eleven':11, 'ten':10, 'nine':9, 'eight':8, 'seven':7, 'six':6, 'five':5, 'four':4, 'three':3, 'two':2}
		

	def test_file_arg(self):
		#Test argument parsers ability to read in a file and parse it
		result = argument_parser(self.file_arg)
		self.assertDictEqual(result, self.proper_alpha_dict, "argument parser failed to find existing file")
		clear_master_index()

	def test_text_blob_arg(self):
		#Test argument parsers ability to parse text passed to it from the command line
		result = argument_parser(self.text_blob_arg)
		self.assertDictEqual(result, self.proper_dict, "argument parser failed to parse passed in text")
		clear_master_index()

if __name__ == '__main__':
	unittest.main()
