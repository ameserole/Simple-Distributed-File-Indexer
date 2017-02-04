# Simple-Distributed-File-Indexer
Command-line indexer application that finds the top 10 words across a collection of documents

##Usage
`python file_indexer.py [-h] text-file [text-file ...] `
  
positional arguments:  
  text-file   List of text files to be indexed  

optional arguments:  
  -h, --help  show help message and exit  

##Example
`python file_indexer.py test-files/artofwar.txt`  
outputs:  
```
Top ten indexed words: 
 1. Word: the     Count: 3813 
 2. Word: of      Count: 2100 
 3. Word: to      Count: 1695 
 4. Word: and     Count: 1479 
 5. Word: in      Count: 1206
 6. Word: a       Count: 1061 
 7. Word: is      Count: 967 
 8. Word: that    Count: 620
 9. Word: be      Count: 612 
10. Word: his     Count: 507
```   
`python file_indexer.py test-files/artofwar.txt test-files/hamlet.txt`  
outputs:
```
Top ten indexed words:
 1. Word: the     Count: 5031
 2. Word: of      Count: 2832
 3. Word: to      Count: 2529
 4. Word: and     Count: 2498
 5. Word: in      Count: 1670
 6. Word: a       Count: 1642
 7. Word: is      Count: 1349
 8. Word: that    Count: 1036
 9. Word: i       Count: 898
10. Word: it      Count: 893
```
`python file_indexer.py --help`  
outputs:  
```
usage: file_indexer.py [-h] text-file [text-file ...]

Simple Distributed File Indexer

positional arguments:
  text-file   List of text files to be indexed

optional arguments:
  -h, --help  show this help message and exit
```

##Testing
Prebuilt tests can be run using the index_tester.py file.  
Usage: `python index_tester.py`  
This program was tested using the index_tester.py file

##Requirements
This program requires python 2.7 or greater to run.  
For help installing python on your system go here:  
https://www.python.org/  
