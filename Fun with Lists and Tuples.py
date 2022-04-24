#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Fun with Lists and Tuples
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
def last(n):
    return n[-1]  
   
def sort(tuples):
    return sorted(tuples, key=last)
   
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sorted:")
print(sort(a))


# In[2]:


def Sort_Tuple(tup):  
        
    # getting length of list of tuples 
    lst = len(tup)  
    for i in range(0, lst):  
            
        for j in range(0, lst-i-1):  
            if (tup[j][-1] > tup[j + 1][-1]):  
                temp = tup[j]  
                tup[j]= tup[j + 1]  
                tup[j + 1]= temp  
    return tup  
    
tup = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
          
print(Sort_Tuple(tup))


# In[ ]:




