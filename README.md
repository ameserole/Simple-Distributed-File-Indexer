# Simple-Distributed-File-Indexer
Command-line indexer application that finds the top 10 words across a collection of documents

##Usage
usage: `file_indexer.py [-h] [-f text-file [text-file ...] | -t text-blob [text-blob ...]]`  

Simple Distributed File Indexer  

arguments:  
  `-h, --help            show this help message and exit`  
  `-f text-file [text-file ...], --files text-file [text-file ...]`  
                        List of text files to be indexed  
 `-t text-blob [text-blob ...], --text text-blob [text-blob ...]`  
                        Blob of text to be indexed   

##Example
`python file_indexer.py test-files/artofwar.txt`  
`python file_indexer.py test-files/artofwar.txt test-files/hamlet.txt`  
`python file_indexer.py -t "This is one Sentence" "This is a second sentence"`  
`python file_indexer.py --help`  

##Testing
Prebuilt tests can be run using the index_tester.py file.  
Usage: `python index_tester.py -b`  
The `-b` suppress standard out. Remove it if you would like to see the print statements that appear while testing
This program was tested using the index_tester.py file

##Requirements
This program requires python 2.7 or greater to run.  
For help installing python on your system go here:  
https://www.python.org/  
