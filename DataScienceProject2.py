#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
import numpy as np
#1. Create a scatter plot of the following data
x=np.array([1,2,3])
y=np.array([1,3,2])

plt.scatter(x,y,color="blue")


# In[3]:


#2
slope_curr1=0
intercept_curr1=0
learning_rate1=0.01
it=10000

for i in range(it):
  y_predicted1=slope_curr1*x+intercept_curr1

  sg1=-(2/3)*sum(x*(y-y_predicted1))
  sc1=-(2/3)*sum(y-y_predicted1)
  slope_curr1=slope_curr1-learning_rate1*sg1
  intercept_curr1=intercept_curr1-learning_rate1*sc1
  plt.plot(x,y_predicted1)
  
plt.scatter(x,y ,color="blue")
plt.plot(x,y_predicted1)


# In[4]:


plt.scatter(x,y,color="red")
plt.plot(x,y_predicted1,color="green")


# In[5]:


x=np.array([1,2])
y=np.array([1,3])

plt.scatter(x,y,color="yellow")


# In[8]:


slope_curr1=0
intercept_curr1=0
learning_rate1=0.01
it=10000

for i in range(it):
  y_predicted1=slope_curr1*x+intercept_curr1

  sg1=-(2/2)*sum(x*(y-y_predicted1))
  sc1=-(2/21)*sum(y-y_predicted1)
  slope_curr1=slope_curr1-learning_rate1*sg1
  intercept_curr1=intercept_curr1-learning_rate1*sc1
  plt.plot(x,y_predicted1)
  
plt.scatter(x,y ,color="blue")
plt.plot(x,y_predicted1)

