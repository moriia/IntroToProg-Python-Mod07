Mariia Kaminskaia
March 1, 2023
IT FDN 110 A Wi 23: Foundations Of Programming: Python
Assignment_07
Link to GitHub: https://github.com/moriia/IntroToProg-Python-Mod07 
Link to GitHub webpage: https://moriia.github.io/IntroToProg-Python-Mod07/

# Pickling and Exception Handling in Python

## Introduction
In this assignment, I had to do research about pickling and Exception handling in Python and create a script to demonstrate the acquired knowledge. This document summarizes the steps I performed to complete the assignment. 


## Creating a script
### Binary files - general
As a part of this assignment, I had to learn and work with a binary file. Binary files are used to store data in the form of bytes, and the method of reading this file is not defined. This means that the program trying to read a binary file needs to be told how to read it. When trying to open a binary file using a normal text editor, it will be shown with unknown or unreadable characters. This is because the text editor assumes the data in text files to be encoded as text. Since the file is not encoded as text, it can not be read by the text editor (source: [https://careerkarma.com/blog/what-is-binary-file/](https://careerkarma.com/blog/what-is-binary-file/)). In general, all files can be classified into two major formats — text and binary. 
As a part of this assignment, I had to create a script that will write and read data into a binary file.

### Pickling in Python
“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy (source: [pickle — Python object serialization](https://docs.python.org/3/library/pickle.html#:~:text=%E2%80%9CPickling%E2%80%9D%20is%20the%20process%20whereby,back%20into%20an%20object%20hierarchy).) There is a built-in pickle library in python (“pickle”), to use it firstly it should be imported (**Figure 1**).



