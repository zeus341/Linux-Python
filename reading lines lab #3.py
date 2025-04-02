# Opening File Handles and reading data from files
print('''
This Lab is about opening a file handle, and reading 
the file, line by line using the file method: 
- file_handle = open(file_name) method
      ''')
# Challenges
print('''
Challenge #1 & #2
----------------------------------------------------
#1 - Edit the code below to count each line, 
     and print the total out at the end
      
#2 - Edit the code below to open the text-file-mail-short.txt file
---

''')
# -------------------------------------------------
print('''Answer to Challenges
-------------------------------------------------''')
# -----------------------------
fhand = open('text-file-mail-very-short.txt')
# You need a variable to count the lines
line_count= 0
for line in fhand:
    # You need to increment the line count Variable
	print(line)
	line_count+=1
	print(line_count)
print('Line Count:', line_count)
print('''
