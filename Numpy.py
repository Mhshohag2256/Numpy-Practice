#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([1,2,3,4,5])
print(a)


# In[2]:


b=np.array([6,7,8,9,10])
print("Addiiton : ",(a+b))
print("Multi : ",(a*b))
print("Subs : ",(b-a))


# In[3]:


c=np.array([[4,5,6],[9,7,2]])


# In[4]:


c


# In[5]:


type(c)


# In[6]:


print(c)


# In[7]:


c.ndim


# In[8]:


a.ndim


# In[9]:


a.shape


# In[10]:


b.shape


# In[11]:


c.shape


# In[12]:


c.dtype


# In[13]:


c.itemsize


# In[14]:


b.itemsize


# In[15]:


c.size


# In[16]:


c.nbytes


# In[18]:


c.dtype


# In[19]:


a.itemsize


# In[20]:


str=np.array(['a','b','ABC'])


# In[21]:


print(str)


# In[23]:


str.dtype


# In[24]:


str.itemsize


# In[25]:


str.nbytes


# In[26]:


y=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])


# In[27]:


y[0,1]


# In[31]:


print(y[0,1:6:2])


# In[34]:


y[0, :]


# In[37]:


y[1,:5]


# In[38]:


y[:,3]


# In[40]:


y[:6,2]


# In[41]:


print(y)


# In[42]:


y[:,3]=[500,600]


# In[43]:


print(y)


# In[45]:


y[1,5]=90


# In[46]:


print(y)


# In[55]:


A=np.zeros((8,1))


# In[56]:


print(A)


# In[57]:


B=np.random.rand(3,2)


# In[58]:


print(B)


# In[59]:


C=np.random.rand(2,3)


# In[60]:


print(C)


# In[65]:


np.ones((3,1))


# In[66]:


np.full((2,2),9)


# In[67]:


np.full((2,4),90)


# In[68]:


print(np.full((9,4),23))


# In[69]:


np.full(3,9)


# In[74]:


np.random.randint(20,size=(4,3))


# In[75]:


np.random.randint(2,6,size=(3,4))


# In[76]:


np.identity(4)


# In[78]:


np.identity(9)


# In[81]:


g=np.array([[1,4,8],[4,9,80],[8,90,53],[3,1,87]])


# In[82]:


print(g)


# In[83]:


g[2,1]


# In[84]:


p=g.copy()


# In[85]:


print(p)


# In[86]:


g[2,1]=9000


# In[87]:


print(g)


# In[88]:


print(p)


# In[89]:


n=np.array([1,2,3,4])


# In[90]:


n-2


# In[91]:


n+5


# In[92]:


n**2


# In[93]:


np.sin(n)


# In[94]:


np.tan(n)


# In[96]:


ab=np.random.randint(10,size=(8,1))
bc=np.random.randint(10,size=(1,8))
print("ab = ",ab,
     "bc = ",bc)


# In[97]:


np.matmul(ab,bc)


# In[99]:


h=np.random.randint(10,size=(3,3))


# In[100]:


print(h)


# In[101]:


np.matinverse(h)


# In[102]:


np.inverse(h)


# In[103]:


np.inv(a)


# In[104]:


inv(a)


# In[107]:


from numpy.linalg import inv


# In[110]:


inv(h)


# In[109]:


inv(h)


# In[ ]:




