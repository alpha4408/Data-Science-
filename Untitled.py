#!/usr/bin/env python
# coding: utf-8

# In[10]:



arr = [[2,3],[5,2],[12,6],[4,4,],[3,5],[8,8]]

arr.insert(0,[2,6])


# In[11]:


arr


# In[12]:


arr.append([2,3])


# In[15]:


arr


# In[18]:


for i in arr:
    for element in i:
        print(i, end = '')


# In[22]:


arr.insert(3,[2,3])


# In[20]:


arr


# In[26]:


for x,y in arr:
    print(y)


# In[27]:


dictsn = {'Age': 20, 'Weight': 195, 'Sex': 'Male'}


# In[32]:


print(dictsn)


# In[33]:


print(dictsn.values)


# In[34]:


x = dictsn['Age']


# In[35]:


x


# In[36]:


type(x)


# In[37]:


dictsn['Age'] = 25


# In[38]:


dictsn


# In[45]:


for x,y in dictsn.items():
    print(x,y)


# In[53]:


for x,y in dictsn.items():
    if x == 'Weight' and y == 195:
        print(f"The {x} of the student is {y} lbs")
        break
     


# In[ ]:




