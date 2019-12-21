#!/usr/bin/env python
# coding: utf-8

# In[10]:


from functools import reduce

list_words = ["India","is","my","country"]

def longestWord(list_words):

 return reduce( (lambda x,y:y if len(y) > len(x) else x), list_words )

print ('Longest word  => ' + longestWord(list_words) )


# In[ ]:





# In[ ]:





# In[ ]:




