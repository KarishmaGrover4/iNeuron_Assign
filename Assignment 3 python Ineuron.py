#!/usr/bin/env python
# coding: utf-8

# ##Assignment 3

# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[1]:


import numpy as np
import matplotlib as mp
ap= int(input("Enter the No. - "))
if (ap==0):
    print(ap, "Zero")
if(ap>0):
    print(ap, "Positive")
if(ap<0):
    print(ap, "Negative")


# 2. Write a Python Program to Check if a Number is Odd or Even?

# In[2]:


ap= int(input("Enter the No. - "))
if (ap%2==0):
    print(ap, "Even")
else:
    print(ap, "Odd")


# 3. Write a Python Program to Check Leap Year?

# In[5]:


import numpy as np
import matplotlib as mp
import calendar

year= int(input("Enter year"))
if (year % 4== 0):
    if(year %100 == 0):
        if(year%400 == 0):
            print(year,"It's a leap year")
        else:
            print(year,"It's not a leap year")
    else: 
        print(year,"It's a leap year")
else:
        print(year,"it's not a leap year")
              
                       


# In[ ]:


import numpy as np
import matplotlib as mp
import calendar

year = int(input("Enter the Year to be checked: "))
if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("%d is Leap Year" %year)
        else:
            print("%d is Not the Leap Year" %year)
    else:
        print("%d is Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)


# 4. Write a Python Program to Check Prime Number?

# In[2]:


a = int(input("Enter the value:"))
if a>1:
        for i in range(2,a):
            if (a % i)==0:
                print(a,"is not a prime no.")
                break
            else:
                print(a, "is a prime no.")
                break
      


# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[3]:


a = 1
b = 10000
for number in range(a,b+1):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)


# In[ ]:





# In[ ]:





# In[ ]:




