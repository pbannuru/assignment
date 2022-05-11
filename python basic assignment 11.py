#!/usr/bin/env python
# coding: utf-8

# 1. Create an assert statement that throws an AssertionError if the variable spam is a negative
# integer.
# 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain
# strings that are the same as each other, even if their cases are different (that is, &#39;hello&#39; and &#39;hello&#39; are
# considered the same, and &#39;goodbye&#39; and &#39;GOODbye&#39; are also considered the same).
# 3. Create an assert statement that throws an AssertionError every time.
# 4. What are the two lines that must be present in your software in order to call logging.debug()?
# 5. What are the two lines that your program must have in order to have logging.debug() send a
# logging message to a file named programLog.txt?
# 6. What are the five levels of logging?
# 7. What line of code would you add to your software to disable all logging messages?
# 8.Why is using logging messages better than using print() to display the same message?
# 9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
# 10.After you click Continue, when will the debugger stop ?
# 11. What is the concept of a breakpoint?

# 1.

# In[10]:


spam = -82
assert spam >=0, 'Variable Spam should not be a -ve number'


# 2.

# In[11]:


def raise_assert(egg,bacon):
    egg = egg.upper()
    bacon = bacon.upper()
    assert not(egg == bacon), 'Eggs/Bacon should not be same, which are same now'


# In[14]:


raise_assert('hello','HELLO')


# In[15]:


raise_assert('goodbye','GOODbye')


# 3.

# In[16]:


def assert_always():
    assert False, 'Always Shows Assertion Error'
assert_always()


# 4.

# In[17]:


import logging
logging.basicConfig(filename = 'application_log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# 5.

# In[18]:


import logging
logging.basicConfig(filename = 'application_log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug("Data Inserted Successfully")
logging.debug('Connection Closed Successfully')
file = open("./application_log.txt","r")
for record in file.readlines():
    print(record)


# 6.The Five levels of Logging provided by python's logging module are CRITICAL(50), ERROR(40), WARNING(30), INFO(20, DEBUG(10), NOTSET(0)

# 7. logging.disable = True

# 8.Post devlopment of your code, you can disable logging messages without removing the logging function, whereas you need to manually remove print() statements, which is tedious activity. and also print is used when you want to display any particular message or help whereas logging is used to record all events like error, info, debug messages, timestamps.

# 9.The Differences between Step Over, Step In, Step Out buttons in debugger are:
# 
# 1.Step in - Step In button will cause the debugger to execute the next line of code and then pause again.
# 
# 2.Step Over - Step Over button will execute the next line of code, similar to the Step In button. However, if the next line of code is a function call, the Step Over button will “step over” the code in the function. The function’s code will be executed at full speed, and the debugger will pause as soon as the function call returns.
# 
# 3.Step out - Step Out button will cause the debugger to execute lines of code at full speed until it returns from the current function.

# 10.This will cause the program to continue running normally, without pausing for debugging untill it terminates or reaches a breakpoint.

# 11. Breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line

# In[ ]:




