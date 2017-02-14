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
`python file_indexer.py -f test-files/artofwar.txt`  
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
`python file_indexer.py -f test-files/artofwar.txt test-files/hamlet.txt`  
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
`python file_indexer.py -t "This is a sentence" "This is another sentence" "This is a third sentence"`  
outputs:
```
Top ten indexed words:
 1. Word: sentence    Count: 3
 2. Word: this        Count: 3
 3. Word: is          Count: 3
 4. Word: a           Count: 2
 5. Word: third       Count: 1
 6. Word: another     Count: 1

```  

`python file_indexer.py --help`  
outputs:  
```
usage: `file_indexer.py [-h] [-f text-file [text-file ...] | -t text-blob [text-blob ...]]`  

Simple Distributed File Indexer  

arguments:  
  `-h, --help            show this help message and exit`  
  `-f text-file [text-file ...], --files text-file [text-file ...]`  
                        List of text files to be indexed  
 `-t text-blob [text-blob ...], --text text-blob [text-blob ...]`  
                        Blob of text to be indexed
```

##Testing
Prebuilt tests can be run using the index_tester.py file.  
Usage: `python index_tester.py -b`  
The `-b` suppress standard out. Remove it if you would like to see the print statements that appear while testing
This program was tested using the index_tester.py file

##Requirements
This program requires python 2.7 or greater to run.  
For help installing python on your system go here:  
https://www.python.org/  
