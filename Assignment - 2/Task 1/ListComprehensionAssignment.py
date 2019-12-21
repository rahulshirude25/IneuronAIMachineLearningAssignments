#!/usr/bin/env python
# coding: utf-8

# In[7]:


#########

word = "ACADGILD"

comp_list = [ alphabet for alphabet in word ]

print(str(comp_list))


input_list = ['x','y','z']

result = [ i*num for i in input_list for num in range(1,5)  ]

print(str(result))



#########

input_list = ['x','y','z']

result = [ i*num for num in range(1,5) for i in input_list  ]

print(str(result))



#########

input_list = [2,3,4]

result = [ [i+num] for i in input_list for num in range(0,3)]

print(str(result))



#########

input_list = [2,3,4,5]

result = [ [i+num for i in input_list] for num in range(0,4)  ]

print(str(result))



#########

input_list=[1,2,3]

result = [ (b,a) for a in input_list for b in input_list]

print(str(result))



#########


# In[ ]:




