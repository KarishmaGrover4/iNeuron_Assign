#!/usr/bin/env python
# coding: utf-8

# ## Assignment 4

# 1. Write a Python Program to Find the Factorial of a Number?

# In[2]:


import math
a= int(input("Enter number: "))
print(math.factorial(a))


# 2. Write a Python Program to Display the multiplication Table?

# In[3]:


a= int(input("Enter the number: "))
print("Multiplication Table of ",a)
for i in range(1,11):
    print(a, 'x', i,'=',a*i)


# 3. Write a Python Program to Print the Fibonacci sequence?
# 

# In[7]:


n = int(input("enter value = "))
n1=0
n2=1
c =0
if(n<0):
    print("enter positive value")
elif n == 1:
        print("print",n)
        print(n1)
else:
    print("Sequence")
    while c < n :
        print(n1)
        a=n1+n2
        n1=n2
        n2=a
        c += 1
                
            
        
        
    


# 4. Write a Python Program to Check Armstrong Number?

# In[1]:


v1= int(input("enter the value: "))
sum = 0
v=v1

while v > 0:
    d = v % 10
    sum += d ** 3
    v //= 10

if v1 == sum:
    print(v1,"Armstrong number")
else:
     print(v1,"not Armstrong number")
        
   


# 5. Write a Python Program to Find Armstrong Number in an Interval?

# In[2]:


v1 = int(input("Enter the lower value: "))
v2 = int(input("Enter the higher value: "))

for i in range(v1, v2 +1):
    pow = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        d = temp %10
        sum += d ** pow
        temp //= 10
        if i == sum:
            print(i)


# 6. Write a Python Program to Find the Sum of Natural Numbers?

# In[22]:


num = int(input("Enter Value"))

if num < 0:
    print("Enter a '+' number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("The sum is", sum) 


# In[ ]:




