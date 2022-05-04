# Test assignment Gennadii Matveev #

## Task #4 - Multiplies of A & B ##

THEORY:  
Multiples of A and B  
Let’s assume that A is 4 and B is 7, so
If we list all the natural numbers below 20 that are multiples of A or B, 
we get 4, 7, 8, 12, 14 and 16.  
TASK:
Create a program that takes a file as the first command line argument. The file content is list of
numbers, with 3 numbers per row separated by space and number of rows is undefined (can
be something between 1 - infinite). First number in a row is A and the second is B, third one is
the goal number (as in theorem 20). The program has to search all multiples of A and B which
are below the third number, print it out to screen and also write results to file which was given
as the second command line argument.  
Program should sort out output file by ascending order how many multiples certain row has.
Example input file content:  
5 8 31  
4 7 20  
Example command line command: python my_program.py input.txt output.txt
Example screen output and output file content:  
20:4 7 8 12 14 16  
31:5 8 10 15 16 20 24 25 30

## Installation Instructions ##
No extra libraries needed - requirements.txt is empty.  
I was using Python 3.10.2, PyCharm on Windows

## Additional info ##

I know how to use parallel opening of two files, but I decided not to use it here 
so that the code would be more understandable.  
From the point of view of OOP, I didn't use classes here, I didn't take out individual 
modules, because it seemed to me that this wasn't important in a small test task and the 
code is visually and logically understandable.

## What program can do (in addition to the basic functionality) ##
* Checks that there are exactly 2 arguments of the script (input and output file) 
* Checks that input and output files have .txt format
* Checks that input file is not empty
* Checks that input file exists (I don't check existence of output file, because here I 
create file with this name or rewrite file with this name)
* Checks that there are 3 numbers in every line of file
* Checks that all three elements in row are integers

## Prepared files ##
* 666.txt - duplicated 3rd numbers, less than needed numbers, 
more than needed numbers, letters instead of numbers
* 555.txt - I was just using it for output (so you can see my last output)
* 444.txt - empty file
* 333.tx - wrong type of file

## Prepared use cases ##
1) python main.py 666.txt 555.txt - will work correctly and list errors
2) python main.py 444.txt 555.txt - will catch empty file error
3) python main.py 777.txt 555.txt - will catch non-existing file error
4) python main.py 333.tx 555.txt - will catch wrong format file error
5) python main.py 555.txt - will catch that there is only one argument

## Spent time ##
I did this program in one day with pauses - real working time about 4 hours.  
I hope that everything is clear. If you have any questions, please email me.