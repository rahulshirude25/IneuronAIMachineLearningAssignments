#!/usr/bin/env python
# coding: utf-8

# In[7]:


def DivideByZero(num1,num2):
    try:
        div=num1//num2;
        print(div);
    except ZeroDivisionError:
        print("divide by zero erro:")
        
def main():
    DivideByZero(5,0);
    
if __name__=="__main__":
    main()


# In[ ]:




