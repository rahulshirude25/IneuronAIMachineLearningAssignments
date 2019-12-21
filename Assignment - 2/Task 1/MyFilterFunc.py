#!/usr/bin/env python
# coding: utf-8

# In[7]:


def myfilter(func,mylist):
    filtoutput=[]
    for i in mylist:
        if func(i):
            filtoutput.append(i)
            
    return filtoutput

myList=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16,17,18]
print(myfilter(lambda num : num % 2 == 0, myList))


            


# In[ ]:





# In[ ]:





# In[ ]:




