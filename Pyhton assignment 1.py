#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("Twinkle, twinkle, little star,")
print("          How I wonder what you are! ")
print("    Up above the world so high, Like a diamond in the ")
print("                       sky. Twinkle, twinkle, little star,")
print("        How I wonder what you are")


# In[8]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[7]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[10]:


from math import pi
rd = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(rd) + " is: " + str(pi * rd**2))


# In[11]:


firstname = input("Input your First Name : ")
lastname = input("Input your Last Name : ")
print ("Hello  " + lastname + " " + firstname)


# In[14]:


num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
# Add two numbers
sum = int(num1) + int(num2)
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# In[ ]:





# In[ ]:




