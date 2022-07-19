#!/usr/bin/env python
# coding: utf-8

# # Import Data

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
from scipy.stats import boxcox


# ## Read In and View

# In[5]:


cruise_ship=pd.read_csv(r"C:\Users\Camille Kenworthy\Downloads\cruise_ship\cruise_ship.csv")


# In[6]:


cruise_ship.head


# In[7]:


pd.options.display.max_columns = None
cruise_ship.head()


# ### Examine All Columns 4 Normailty

# In[8]:


sns.pairplot(cruise_ship)


# ### Transform Positvely Skewed Data Tonnage

# In[9]:


cruise_ship['TonnageSQRT'] = np.sqrt(cruise_ship['Tonnage'])


# In[10]:


cruise_ship.head()


# In[11]:


cruise_ship.TonnageSQRT.hist()


# In[12]:


cruise_ship['TonnageLOG'] = np.log(cruise_ship['Tonnage'])


# In[13]:


cruise_ship.head()


# In[14]:


cruise_ship.TonnageLOG.hist()


# #### Cabins

# In[15]:


cruise_ship['CabinsSQRT'] = np.sqrt(cruise_ship['Cabins'])


# In[16]:


cruise_ship.head()


# In[17]:


cruise_ship.CabinsSQRT.hist()


# ##### Passengers 

# In[18]:


cruise_ship['passngrsSQRT'] = np.sqrt(cruise_ship['passngrs'])


# In[19]:


cruise_ship.head()


# In[20]:


cruise_ship.passngrsSQRT.hist()


# # Crew

# In[22]:


cruise_ship['CrewSQRT'] = np.sqrt(cruise_ship['Crew'])
cruise_ship.head()
cruise_ship.CrewSQRT.hist()


# ## PassSpcR

# In[23]:


cruise_ship['PassSpcRSQRT'] = np.sqrt(cruise_ship['PassSpcR'])
cruise_ship.head()
cruise_ship.PassSpcRSQRT.hist()


# ## OutCab

# In[24]:


cruise_ship['outcabSQRT'] = np.sqrt(cruise_ship['outcab'])
cruise_ship.head()
cruise_ship.outcabSQRT.hist()


# In[25]:


cruise_ship['outcabLOG'] = np.log(cruise_ship['outcab'])
cruise_ship.head()
cruise_ship.outcabLOG.hist()


# # Transform Negatively Skewed  Data 

# # Year Built

# In[26]:


cruise_ship['YearBltSQ'] = cruise_ship['YearBlt']**2
cruise_ship.head()
cruise_ship.YearBltSQ.hist()


# In[27]:


cruise_ship['YearBltCUBE'] = cruise_ship['YearBlt']**3
cruise_ship.head()
cruise_ship.YearBltCUBE.hist()


# # Lengeth

# In[28]:


cruise_ship['LengthSQ'] = cruise_ship['Length']**2
cruise_ship.head()
cruise_ship.LengthSQ.hist()


# In[29]:


cruise_ship['LengthCUBE'] = cruise_ship['Length']**3
cruise_ship.head()


# In[30]:


cruise_ship.LengthCUBE.hist()


# In[ ]:




