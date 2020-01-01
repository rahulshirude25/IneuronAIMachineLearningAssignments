#!/usr/bin/env python
# coding: utf-8

# In[12]:


def generateSentences():
    subjects=["Americans ","Indians"]
    verbs=["play","watch"] 
    objects=["Baseball","Cricket"] 
    for i in range(len(subjects)):
        for j in range(len(verbs)):
            for k in range(len(objects)):
                print(subjects[i],"",verbs[j],"",objects[k],end=".\n");
                
generateSentences()


# In[ ]:





# In[ ]:




