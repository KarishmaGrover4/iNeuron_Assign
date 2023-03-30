#!/usr/bin/env python
# coding: utf-8

# ## Assignment 1

# 
#     Write a Python program to print "Hello Python"?
# 
# 

# In[ ]:


c= "Hello Python"
print(c)


# 2. Write a Python program to do arithmetical operations addition and division.?

# In[ ]:


n1 = int(input("Enter 1st no."))
n2 = int(input ("Enter 2nd no."))
Add = n1 + n2
div = n1 / n2
print('Add =',Add,'\n','Div =',div)


# 3. Write a Python program to find the area of a triangle?

# In[ ]:


b1= int(input("Enter breadth"))
h1= int(input("Enter height"))
right_angle_triangle_area = (1/2)*(b1*h1)
print('Area of right angle Triangle = ',right_angle_triangle_area)


# In[ ]:


b1= int(input("Enter breadth"))
l1= int(input("Enter lenghth"))
h1= int(input("Enter height"))
s= (l1+b1+h1)/2
area = (s*(s-b1)*(s-h1)*(s-l1))**(0.5)
print('Area of Triangle = ',area)


# 4. Write a Python program to swap two variables?

# In[ ]:


a=int(input("enter 1st variable"))
b=int(input("enter 2nd variable"))
temp=a
a=b
b=temp
print('1st no =',a,'2nd no =',b)
    


# 5. Write a Python program to generate a random number?

# In[ ]:


import random
num = random.random()
print(num)
list=[1,2,3,4,5]
print(random.choice(list))
my_word="karishma"
print(random.choice(my_word))


# In[ ]:





# In[ ]:




