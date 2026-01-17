#!/usr/bin/env python
# coding: utf-8

# **Practical:** Data Aggregation and it Types with Time & Spatial Aggregation in Data Mining

# In[63]:


import pandas as pd


# In[64]:


#step1: Creating Sample Dataset

Data_Abhishek={
    'Region':['North','South','East','West','North','East','West','South','West','East'],
    'Product':['A','B','C','A','D','D','A','C','B','B'],
    'Sales':[150,200,400,250,180,220,310,500,156,777],
    'Quantity':[10,15,20,16,7,18,45,30,25,3]
}


# In[65]:


df=pd.DataFrame(Data_Abhishek)
print("Sample Dataset:\n",df)


# **##step2: Grouping  & Aggregating**

# In[66]:



#Aggregating Sales by Region(Sum Aggregation)
sales_by_region_Abhishek=df.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:\n",sales_by_region_Abhishek)


# In[67]:


#Aggregating sales & Quantity by product(Mean)
mean_by_product_Abhishek=df.groupby('Product')[['Sales','Quantity']].mean()
print("\nMean Sales Quantity by Product:\n",mean_by_product_Abhishek)


# In[68]:


#Aggregating Count of sales by region(Count aggregation)

Count_by_region_Abhishek=df.groupby('Region')['Sales'].count()
print("\nCount of Sales Records by Region:\n",Count_by_region_Abhishek)


# In[69]:


#custom Agregation : Calculate Min & Max Sales by Region
custom_aggregation_Abhishek=df.groupby('Region')["Sales"].agg(['min','max'])
print("\nCustom Aggregation (Minimum & Maximum Sales by Region):\n",custom_aggregation_Abhishek)


# **##Step 3 : Multi-Level Aggregation**

# In[70]:


#Aggregation Sales by Region & Product
multi_level_agg_Abhishek=df.groupby(['Region','Product'])['Sales'].sum()
print("\nSales by Region & Product :\n",multi_level_agg_Abhishek)


# **Step 4 : Reset Index For Multi - Level Aggregation**

# In[71]:


multi_level_agg_reset_Abhishek=multi_level_agg_Abhishek.reset_index()
print("\nSales by Region & Product (Reset Index):\n",multi_level_agg_reset_Abhishek)


# **Objective :**
# 
# - To understand and implement :
# - *Time Aggregation : Aggregating data over different time periods(eg.Month, year)*
# 
# - *Spatial Aggregation: Aggregating data by Spatial Attributies(eg. by region,city)*

# In[72]:


import pandas as pd 


# In[84]:


data1_Abhishek={
    'Region':['North','South','East','West','North','East','West','South','West','East'],
    'Product':['A','B','C','A','D','D','A','C','B','B'],
    'Sales':[150,200,400,250,180,220,310,500,156,777],
    'Quantity':[10,15,20,16,7,18,45,30,25,3],
    'City': ['City1', 'City2', 'City3', 'City4', 'City1', 'City2', 'City3', 'City4','City1','City7'],
    'Date':pd.to_datetime(['2024-01-01', '2024-01-02', '2024-02-01', '2024-02-03','2024-03-01',
                           '2024-03-02', '2024-04-01', '2024-04-03','2024-05-25','2024-05-16'])
}


# In[85]:


df_Abhishek=pd.DataFrame(data1_Abhishek)
print("Extended Dataset:\n",df_Abhishek)


# ## Time Aggregation

# In[86]:


#set data Column as Index
df_Abhishek.set_index('Date',inplace=True)


# In[87]:


print(df_Abhishek)


# In[88]:


#Aggregating Sales by Month
monthly_sales_Abhishek=df_Abhishek.resample('M')['Sales'].sum()
print("\nTotal Sales by Month :\n",monthly_sales_Abhishek)


# In[89]:


#Aggregating Sales by Quater
quaterly_sales_Abhishek=df_Abhishek.resample('Q')['Sales'].sum()
print("\nTotal Sales by Quater :\n",quaterly_sales_Abhishek)


# In[90]:


#Aggregating Sales by Year
yearly_sales_Abhishek=df_Abhishek.resample('Y')['Sales'].sum()
print("\nTotal Sales by Year :\n",yearly_sales_Abhishek)


# In[91]:


#Reset Index To Restore Original Structure
df_Abhishek.reset_index(inplace=True)


# # Spatial Aggregation:
# 

# In[92]:


#Aggregating Sales by Region
sales_by_region_Abhishek=df_Abhishek.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:\n", sales_by_region_Abhishek)


# In[93]:


#Aggregating Sales by City
sales_by_city_Abhishek=df_Abhishek.groupby('City')['Sales'].sum()
print("\nTotal Sales by City:\n", sales_by_city_Abhishek)


# In[95]:


# Aggregating Sales by Region and City
sales_by_region_city_Abhishek = df_Abhishek.groupby(['Region', 'City'])['Sales'].sum()
print("\nTotal Sales by Region and City:\n", sales_by_region_city_Abhishek)


# # Step4: Export Spatial Aggregation Results
# 

# In[97]:


sales_by_region_city_reset_Abhishek=sales_by_region_city_Abhishek.reset_index()

print(sales_by_region_city_reset_Abhishek)


# In[98]:


sales_by_region_city_reset_Abhishek.to_csv("spatial_aggregation.csv", index=False)
print("\nSpatial aggregation data saved to 'spatial_aggregation.csv'")


# In[ ]:




