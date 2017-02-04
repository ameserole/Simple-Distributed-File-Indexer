# Simple-Distributed-File-Indexer
Command-line indexer application that finds the top 10 words across a collection of documents

##Usage
python file_indexer.py [-h] text-file [text-file ...]  
  
positional arguments:  
  text-file   List of text files to be indexed  

optional arguments:  
  -h, --help  show this help message and exit  

##Example
`python file_indexer.py test-files/artofwar.txt`  
`python file_indexer.py test-files/artofwar.txt test-files/hamlet.txt`  
`python file_indexer.py --help`

##Testing
Prebuilt tests can be run using the index_tester.py file.  
Usage: `python index_tester.py`  
This program was tested using the index_tester.py file

##Requirements
This program requires python 2.7 or greater to run.  
For help installing python on your system go here:  
https://www.python.org/  
