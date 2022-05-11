#!/usr/bin/env python
# coding: utf-8

# 1. Is the Python Standard Library included with PyInputPlus?
# 2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
# 3. How do you distinguish between inputInt() and inputFloat()?
# 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
# 5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
# 6. If a blank input is entered three times, what does inputStr(limit=3) do?
# 7. If blank input is entered three times, what does inputStr(limit=3, default=&#39;hello&#39;) do?

# 1.it is not a part of python standard library

# 2.this piece of code help us save time from calling each time we want to use pyinputplus where pypi is allias

# 3.inputInt() is for integers i.e number without decimal
# where as inputFloat() belongs to float class i.e with decimal.

# 4.

# In[3]:


import pyinputplus as pyip
wholenumber = pyip.inputInt(prompt='Enter a number: ', min=0, max=100)
print(wholenumber)


# 5. we can use allowRegexes and blockRegexes keyword arguments to take list of regular expression strings to determine what the pyinputplus function will reject or accept valid input.

# 6. The statement inputStr(limit=3) will throw two exceptions ValidationException and RetryLimitException. The first exception is thrown because blank values are not allowed by inputStr() function by default. it we want to consider blank values as valid input, we have to set blank=True.
# 
# The second exception is occured because we have reached the max limit we have specified by using limit parameter. inorder to avoid this exception we can use default parameter to return a default value when max limit is reached.

# 7.Since the default parameter is set to hello. after blank input is entered three times instead of raising RetryLimitException exception. the function will return hello as response to the calling function

# In[ ]:




