#!/usr/bin/env python
# coding: utf-8

# 1. To what does a relative path refer?
# 2. What does an absolute path start with your operating system?
# 3. What do the functions os.getcwd() and os.chdir() do?
# 4. What are the . and .. folders?
# 5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
# 6. What are the three “mode” arguments that can be passed to the open() function?
# 7. What happens if an existing file is opened in write mode?
# 8. How do you tell the difference between read() and readlines()?
# 9. What data structure does a shelf value resemble?

# 1.The relative path is the path to some file with respect to your current working directory (PWD).
# For example: if Absolute path to a file called stuff.txt is: C:/users/admin/docs/stuff.txt If my PWD is C:/users/admin/ , then the relative path to stuff.txt would be: docs/stuff.txt
# Note: PWD + relative path = absolute path

# 2.In Linux based systems the absolute path starts with /. Where as in Windows based systems absolute path starts with C:

# 3.os.getcwd() method tells us the location of current working directory (CWD). Whereas os.chdir() method in Python used to change the current working directory to specified path. These functions are similar to linux commands pwd and cd

# 4.. Represents the Current Directory Whereas .. Represents the Parent Directory of the Current Directory
# For Example: if the below path is my absolute path:
# C:\\Users\\vishnu\\Documents\\iNeuron-Assignments\\Python Basic Assignment
# Then . represents the path C:\\Users\\vishnu\\Documents\\iNeuron-Assignments\\Python Basic Assignment
# Where as .. represents the path C:\\Users\\vishnu\\Documents\\iNeuron-Assignments

# 5. For C:\bacon\eggs\spam.txt
# 
# The dir name is C:\\bacon\\eggs
# 
# The Base name is spam.txt

# 6.A file can be Accessed in python using open() function. open function takes two arguments filename and mode of operation (optional). if mode is not provided the default mode of opening is read mode
# So, the syntax being: open(filename, mode)
# 
# ‘r’ – Read Mode: This is the default mode for open(). The file is opened and a pointer is positioned at the beginning of the file’s content.
# ‘w’ – Write Mode: Using this mode will overwrite any existing content in a file. If the given file does not exist, a new one will be created.
# ‘r+’ – Read/Write Mode: Use this mode if you need to simultaneously read and write to a file.
# ‘a’ – Append Mode: With this mode the user can append the data without overwriting any already existing data in the file.
# ‘a+’ – Append and Read Mode: In this mode you can read and append the data without overwriting the original file.
# ‘x’ – Exclusive Creating Mode: This mode is for the sole purpose of creating new files. Use this mode if you know the file to be written doesn’t exist beforehand.

# 7.Using this mode will overwrite any existing content in a file. If the given file does not exist, a new one will be created.

# 8.The main difference is that read() will read the whole file at once and then print out the first characters that take up as many bytes as you specify in the parenthesis
# 
# Whereas the readline() that will read and print out only the first characters that take up as many bytes as you specify in the parenthesis. You may want to use readline() when you're reading files that are too big for your RAM.
# The read() would treat each character in the file separately, meaning that the iteration would happen for every character.
# The readline() function, on the other hand, only reads a single line of the file. This means that if the first line of the file were three lines long, the readline() function would only parse (or iterate/operate) on the first line of the file.

# 9. it contains key and values it represents dictionary.

# In[ ]:




