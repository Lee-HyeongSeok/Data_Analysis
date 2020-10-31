#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


df = pd.read_csv("D:\python_data\ch1_sport_test.csv",
                index_col="학생번호")


# In[5]:


df


# In[6]:


df['악력']


# In[8]:


df['윗몸일으키기']


# In[9]:


df.shape


# In[ ]:




