#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Make Your Own mini-Dictionary
#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

# Create the dictionary
my_dict = {}
 
# Now populate it
for i in range(97, 97 + 26):
    # Map character to ascii value
    my_dict[chr(i)] = i
 
print(my_dict)


# In[2]:


my_dict = {chr(i): i for i in range(97, 97 + 26)}
print(my_dict)


# In[ ]:




