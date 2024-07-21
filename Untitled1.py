#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[36]:


pwd


# In[37]:


Dataset = pd.read_csv(r"C:\Users\macbo\Documents\Diwali_Sales_Data.csv", encoding=('ISO-8859-1'))


# In[38]:


Dataset.head(20)


# In[39]:


Dataset.shape


# In[40]:


Dataset.head(10) 


# In[41]:


Dataset.info()


# In[42]:


Dataset.drop(['Status','unnamed1'], axis=1, inplace=True)


# In[43]:


Dataset.info()


# In[44]:


pd.isnull(Dataset)


# In[45]:


pd.isnull(Dataset).sum()


# In[116]:


Dataset.info()


# In[47]:


Dataset['Amount'].dtypes


# In[48]:


Dataset.columns


# In[49]:


# rename column   
Dataset.rename(columns= {'Marital_Status':'Shaadi'})


# In[50]:


# describe ()method returns description of the data in the dataframe(i.e. count, mean , std,etc)
Dataset.describe()


# In[51]:


Dataset[['Age','Orders','Amount']].describe()


# In[52]:


ax = sns.countplot(x = 'Gender',data = Dataset)


# In[53]:


ax = sns.countplot(x = 'Gender' ,data = Dataset)
for bars in ax.containers:
    ax.bar_label(bars)


# from above greapgy we can see tat most of tyhe buyers are womans and purchasing power of females are higher than mens   

# # Age

# In[143]:


Dataset.columns


# In[23]:


ax = sns.countplot(data = Dataset, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# from above graphs we can see that mpost of the buyers are of age group between 26-35 years female

# In[57]:


# Total Amount vs Age group
sales_age = Dataset.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x ='Age Group',y= 'Amount',data = sales_age) 


# In[ ]:


From above graphs we can see that mpost of the buyers are of age group between 26-35 years female


# # State

# In[85]:


# total number of orders from top 10 states
sales_state = Dataset.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10) 
sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(data = sales_state, x='State',y='Orders')


# In[88]:


# total amount/sales from top 10 states
sales_state = Dataset.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10) 
sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(data = sales_state, x='State',y='Amount')


# In[102]:


ax = sns.countplot(data = Dataset, x = 'Marital_Status')
sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[104]:


sales_state = Dataset.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10) 
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x='Marital_Status',y='Amount',hue='Gender')


# #Occupation

# In[114]:


ax = sns.countplot(data = Dataset, x = 'Occupation')
sns.set(rc={'figure.figsize':(20,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[120]:


sales_state = Dataset.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation' , y = 'Amount') 


# from above graphs we can see that the most of the buyers areworkingh in it healthcare anmd avaition

# # Product category

# In[134]:


ax = sns.countplot(data = Dataset, x = 'Product_Category')
sns.set(rc={'figure.figsize':(28,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[139]:


sales_state = Dataset.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(25,8)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# from above graphs we can see that the most of the sold products are from food ,clothing and electronic category

# In[144]:


sales_state = Dataset.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')                               


# In[145]:


#top 10 most sold products(same thing as above)
fig1, ax1 =plt.subplots(figsize=(12,7))
Dataset.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion

# Married woman age group 26-35 yrs from UP,Maharasta and Kamatake working in IT,Healthcare and Avaition are more likely to buy products from food clothing and Electronic category

# In[ ]:




