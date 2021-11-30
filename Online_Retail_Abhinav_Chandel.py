#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import io


# ## Reading the file

# In[2]:


df = pd.read_excel('Online Retail.xlsx')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.describe(include='all', datetime_is_numeric=True).T


# In[7]:


df.shape


# In[8]:


df.isnull().sum()


# In[9]:


df.duplicated().sum()


# In[10]:


df[df.duplicated()]


# In[11]:


df['Target'] = df['UnitPrice'] * df['Quantity']
df['Target']


# ## EDA - Univariate and Bivariate analysis

# In[12]:


def univariateAnalysis_numeric(column, nbins):
  
    print("Description of " + column)
    print("-------------------")
    print(df[column].describe(),end=' ')
    print('/n')
    
    
    plt.figure()
    print("Distribution of " + column)
    print('-------------------')
    sns.distplot(df[column], kde=True, color='black');
    plt.show()
    
    plt.figure()
    print("Boxplot of " + column)
    print('-------------------')
    ax = sns.boxplot(x=df[column],color='green')
    plt.show()


# In[13]:


import matplotlib.pyplot as plt
import seaborn as sns

df_num = df.select_dtypes(include = ['float64', 'int64'])
lstnumericcolumns = list(df_num.columns.values)
len(lstnumericcolumns)

for x in lstnumericcolumns:
    univariateAnalysis_numeric(x,16)


# In[14]:


plt.figure(figsize=(15,10))
df.boxplot()


# In[20]:


df.head()


# In[24]:


plt.figure(figsize=(15,10))
sns.barplot(data = df, x='Target', y='Country',ci=None)


# From this EDA we can see that the Total sales is maximum for Netherlands followed by Australia, whereas, USA has the least sales in the given data

# In[19]:


plt.figure(figsize=(20,12))
sns.heatmap(df.corr(),annot=True)
plt.show()


# There is a linear relation betwee the Total Sales and the Quantity and least correlation between the Unit Price with the same target variable.

# ---THE END---
