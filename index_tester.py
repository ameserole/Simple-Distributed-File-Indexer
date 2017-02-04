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
		result = text_parser(file)
		self.assertEqual(result, self.sentence_list, "text_parser tokenized the words in sentence.txt wrong")

	def test_non_alphanum_delimit(self):
		#Test parser on text with several special characters
		file = open('test-files/non-alpha-num.txt', 'r')
		result = text_parser(file)
		self.assertEqual(result, self.alphanum_list, "text_parser tokenized the words in non-alpha-num.txt wrong")

	def test_numbers(self):
		#Test parser on a sentence with numbers in it
		file = open('test-files/number-test.txt', 'r')
		result = text_parser(file)
		self.assertEqual(result, self.number_list, "text_parser tokenized the words in number-test.txt wrong")

class test_word_indexer(unittest.TestCase):
	def setUp(self):
		self.word_list = ['one','two','two','three','three','three','four','four','four','four','five','five','five','five','five',
						  'six', 'six', 'six', 'six', 'six', 'six', 'seven', 'seven', 'seven', 'seven', 'seven', 'seven', 'seven',
						  'eight','eight','eight','eight','eight','eight','eight','eight','nine','nine','nine','nine','nine','nine',
						  'nine','nine','nine','ten','ten','ten','ten','ten','ten','ten','ten','ten','ten', 'eleven', 'eleven', 'eleven'
						  , 'eleven', 'eleven', 'eleven', 'eleven', 'eleven', 'eleven', 'eleven', 'eleven']
		
		self.word_list_mixed_case = ['One','two','twO','three','Three','Three','four','four','FOUR','four','five','five','five','five','five',
						  'six', 'six', 'six', 'six', 'six', 'siX', 'seven', 'seven', 'seven', 'seven', 'seven', 'seven', 'seven',
						  'eight','eight','EIGHT','eIght','eiGht','eight','eight','eight','nine','nine','nine','nine','nIne','nine',
						  'nine','nine','ninE','ten','ten','TEN','ten','ten','ten','ten','ten','ten','ten', 'eleven', 'eleven', 'eleven'
						  , 'eleven', 'eleven', 'eleven', 'eleven', 'ELEVEN', 'eleven', 'eleven', 'eleveN']

		self.proper_dict = {'eleven':11, 'ten':10, 'nine':9, 'eight':8, 'seven':7, 'six':6, 'five':5, 'four':4, 'three':3, 'two':2}

	def test_word_list(self):
			#Test word indexer on a list of all lower case words
			result = word_indexer(self.word_list)
			self.assertEqual(result, self.proper_dict, "word_indexer did not properly index the words")
			clear_master_index()	#Clear the master index in file_indexer.py so that the results of using word_indexer in each test arent felt in others

	def test_word_list_mixed_case(self):
			#Test word indexer on a list of mixed case words
			result = word_indexer(self.word_list_mixed_case)
			self.assertEqual(result, self.proper_dict, "word_indexer did not properly index the words with mixed cases")
			clear_master_index()	#Clear the master index in file_indexer.py so that the results of using word_indexer in each test arent felt in others


if __name__ == '__main__':
    unittest.main()