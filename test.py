#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
df=pd.read_excel("Desktop/census_2011.xlsx")


# In[7]:


df


# In[8]:


df.columns


# In[17]:


import pandas as pd
df=pd.read_excel("Desktop/census_2011.xlsx")
df.rename(columns={'State name':'State/UT'})
df.rename(columns={'District name':'District'})
df.rename(columns={'Male_Literate':'Literate_Male'})
df.rename(columns={'Female_Literate':'Literate_Female'})
df.rename(columns={'Rural_Households':' Households_Rural'})
df.rename(columns={'Urban_ Households':'Households_Urban'})
df.rename(columns={'Age_Group_0_29':'Young_and_Adult'})
df.rename(columns={'Age_Group_30_49':'Middle_Aged'})
df.rename(columns={'Age_Group_50':'Senior_Citizen'})
df.rename(columns={'Age not stated':'Age_Not_Stated'})


# In[16]:


df.columns


# In[24]:


import pandas as pd
df=df.rename(columns={'State name':'State/UT','District name':'District','Male_Literate':'Literate_Male','Female_Literate':'Literate_Female','Rural_Households':' Households_Rural','Urban_ Households':'Households_Urban','Age_Group_0_29':'Young_and_Adult','Age_Group_30_49':'Middle_Aged','Age_Group_50':'Senior_Citizen','Age not stated':'Age_Not_Stated'})


# In[25]:


df.columns


# In[28]:


import pandas as pd
df=pd.read_excel("Desktop/census_2011.xlsx")


# In[ ]:





# In[ ]:




