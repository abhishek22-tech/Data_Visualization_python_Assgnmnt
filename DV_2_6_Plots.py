#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(200,6),index= pd.date_
range('1/9/2009', periods=200), columns= list('ABCDEF'))
df.plot(figsize=(20, 10)).legend(bbox_to_anchor=(1, 1))


# In[5]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb',
'March','April', 'May'])
df.plot.bar(figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


# In[10]:


df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb',
'March','April', 'May']) 
df.plot.bar(stacked=True,
figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


# In[9]:


df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb',
'March','April', 'May']) 
df.plot.barh(stacked=True,
figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


# In[12]:


df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb',
'March','April', 'May'])
df.plot.hist(bins= 20, figsize=(10,8)).legend(bbox_to_anchor=(1.2, 1))


# In[13]:


df=pd.DataFrame({'April':np.random.randn(1000)+1,'May':np.random.
randn(1000),'June': np.random.randn(1000) - 1}, columns=['April',
'May', 'June'])
df.hist(bins=20)


# In[14]:


df = pd.DataFrame(np.random.rand(20,5),
columns=['Jan','Feb','March','April', 'May'])
df.plot.box()


# In[16]:


df = pd.DataFrame(np.random.rand(20,5),
columns= ['Jan','Feb','March','April', 'May'])
df.plot.area(figsize=(6, 4)).legend(bbox_to_anchor=(1.3, 1))


# In[18]:


df = pd.DataFrame(np.random.rand(20,5),columns= ['Jan','Feb',
'March','April', 'May'])
df.plot.scatter(x='Feb', y='Jan', title='Temperature over two months ')


# In[ ]:




