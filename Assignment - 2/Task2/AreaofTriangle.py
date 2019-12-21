#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Triangle:

 def __init__(self, lenA, lenB, lenC):

  self.side1 = lenA

  self.side2 = lenB

  self.side3 = lenC




class Triangle_Func(Triangle):

 

 def __init__(self, side1, side2, side3):

  

  super(Triangle_Func, self).__init__(side1, side2, side3)



 def get_area(self):

  s = (self.side1 + self.side2 + self.side3)/2

  return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5



instance = Triangle_Func(4,5,6)

print ("Area of triangle = " + str(instance.get_area()) )


# In[ ]:




