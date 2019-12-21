#!/usr/bin/env python
# coding: utf-8

# In[3]:


def myreduce(function, iterable):
    it = iter(iterable)
    result=next(it)
    for x in it:
        result = function(result, x)
    return result

my_list=[1,2,3,4,5]
print(myreduce(lambda x,y:x*y,my_list))


# In[ ]:





# In[ ]:




