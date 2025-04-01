# Opening File Handles and reading data from files
# You can get the following files with wget
# sudo wget -O text-flie-matrix.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-matrix.txt
# sudo wget -O text-file-mail-very-short.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-mail-very-short.txt
print('''
This Lab is about opening a file handle, and 
printing the file handle.

Hint: Check out W3Schools File Handling
- https://www.w3schools.com/python/python_file_handling.asp
      ''')
# Challenge 1
# Describe the parts of the file handle
print('''
Challenge # 1
----------------------------------------------------
Can you explain each part of the file handle? 

What does the following parts of the file handle mean?
1) _io.TextIOWrapper 
2) name='matrix.txt' 
3) mode='r' 
4) encoding='UTF-8'>
      
Hint: https://www.w3schools.com/python/python_file_handling.asp
---
''')
# -------------------------------------------------
print('''Answer to Challenge 1
-------------------------------------------------''')
# What does the following parts of the file handle mean?
# 1) _io.TextIOWrapper : This means the type of object the text file returns to, using the TextIOWrapper to provide text
# 2) name='text-file-matrix.txt' : The name of the file and which it will be defined as
# 3) mode='r' : Refers to the specfics in which the file is opened r being to read, only thing you could do is read the file.
# 4) encoding='UTF-8'> : Specficially refers to encoding the file, wbich will be used to encode it using the unicode standard
# print('The parts of a file handle are:')
# -----------------------------
xfile = open('text-file-matrix.txt')
print(xfile)
print('')
