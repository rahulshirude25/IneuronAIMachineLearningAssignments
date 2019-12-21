#!/usr/bin/env python
# coding: utf-8

# In[5]:


def vowel_check(char):

 if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
  return True
 else:
  return False

char = input("Enter character: ");
if (char.isalpha() == False):
 exit();

if (vowel_check(char)):
 print(char, "is a vowel.");
else:
 print(char, "is not a vowel."); 


# In[ ]:




