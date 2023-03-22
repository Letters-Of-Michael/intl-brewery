#!/usr/bin/env python
# coding: utf-8

# # We start by importing the needed libraries

# In[1]:

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


header = st.container()
background = st.container()
Data_Development = st.container()
dataset = st.container()
question = st.container()
visualization = st.container()
inference = st.container()
copywright = st.container()


# # Importing our file into python and reading it

# In[2]:

with header:
	st.title('INTERNATIONAL BREWERY')
	st.write('An extensive analysis to provide general insights about the business year from the data provided by the international brewery. The data analyzed gave an overall insight about the operations of the company, from production to logistics to delivery. The analysis was carried out using python on jupyter notebook') 

	img = Image.open("./image/1.png")
	st.image(img)

	img = Image.open("./image/2.png")
	st.image(img)

	with background:
		st.text("This is how our data looks like after importing into a dataframe.")
		#brewery_df = pd.read_csv('./image/international2.csv')
	
	with open('image/international.csv.zip', 'rb') as fp:
		st.download_button(label = 'Download dataset', data = fp, file_name = 'brewery_sales.zip', mime='application/zip', help = 'This allows you to download the complete dataset')
# In[3]:


		#brewery_df


# # Getting an overall information about our data, to note mistakes and propably any incoplete cell

# In[4]:


#to have the index removed use:
#brewery_df = pd.read_csv('./intl/international brewery pp.csv', index_col = "Year")


	with Data_Development:
		st.header('Data Development')
		st.write("The data was supplied by the company and after importing with python, we set out to doing some data manipulation and development before we set out to visualize our data. Our data visualization will be centred around the question we were given to answer by the comapny.")
	



#to check for missing values
brewery_df.isnull()


# In[5]:


#to get a summary of missing values
brewery_df.isnull().sum()


# In[6]:


#to check for any missing values
brewery_df.isnull().values.any()


# In[7]:


#to check total number for any missing values
brewery_df.isnull().sum().sum()


# In[8]:


#to fill the spaces up


# In[9]:

with dataset:
		st.write("Here, we describe, get more info about our dataset, we checked for null values and tried to replace it. We can do this in three ways:")
		st.markdown('* **First:** We replace null values with the mean value, if we have a large dataset and large number of null sets.')
		st.markdown('* **Second:** We simply remove the cells with null values if they are insignificant.')
		st.markdown('* **Third:** We ask or make enquiry from the data source and simply replace with the accurate values')

		st.header('Describing Object Types')

		img = Image.open("./image/7.png")
		st.image(img)

		brewery_df.dtypes


# In[10]:


brewery_df.describe()


st.write('We called out the columns, to have a clear understanding and we called out the shape of the table so as to know the number of columns and rows we are dealing with.')

brewery_df.columns, brewery_df.shape


# In[13]:

st.write('In these cells, we called out certain columns so as to understand the relationship between each cells.')
#lets call the volume with the year

img = Image.open("./image/8.png")
st.image(img)
brewery_df['Volume']


# In[14]:


#lets call the truck size and volume
img = Image.open("./image/9.png")
st.image(img)
brewery_df[['Truck_Size', 'Volume']]


# In[15]:


#lets make a copy of our big table 
brewery_copy_df = brewery_df.copy()


# In[16]:

st.write('I went further to get a feel of our table after all manipulations have been done, with this, I called out random cells, the first and the last 10 values. Furthermore, I accessed specific cells and also a range of datasets from 2411 to 2420, these are efforts and ways to get a grab and feel of what our dataset looks like.')
brewery_df.loc[2411]


#to access a specific cell
st.write('To access the content of a specific cell.')

img = Image.open("./image/13.png")
st.image(img)
brewery_df.at[36171, 'Truck_Size']


# In[20]:

st.write('Cells from 2411 to 2420')
brewery_df.loc[2411:2420]

st.header('ANALYSIS AND VISUALIZATION')
st.write("We begin by laying out questions we want to find answers to, this will be my guide as to what and what and the type of codes to write, the best type of visualization to effectively pass the message across.")
# # Time to analyze and drive out necesarry data to answer our quesions
st.markdown('* **1.** What is the total sales volume per Truck size?')
st.markdown('* **2.** What is monthly sales volume recorded in the course of production?')
st.markdown('* **3.** What is the total volume and percentage volume returned and retained?')
st.markdown('* **4.** What is the total volume moved by trucks owned, hired and dedicated to the comapny?')
st.markdown('* **5.** What is the volume produced according to each load type?')
st.markdown('* **6.** What quantity of volume is being prouced by each depot?')


#Question 1
st.write('Question 1')

img = Image.open("./image/16.png")
st.image(img)
Truck_Size_volume_groups = brewery_df.groupby('Truck_Size')
TTruck_Size = Truck_Size_volume_groups[['Volume']].count()
TTruck_Size


# In[41]:


import streamlit as st
st.bar_chart(TTruck_Size)


# In[31]:


#Question 2
st.write('Question 2')

img = Image.open("./image/17.png")
st.image(img)

Month_volume_groups = brewery_df.groupby('Month')
Sum_months_volume_df = Month_volume_groups[['Volume']].sum()
Sum_months_volume_df


# In[43]:


st.line_chart(Sum_months_volume_df)


# In[33]:


#Question 3
st.write('Question 3')

img = Image.open("./image/18.png")
st.image(img)

Returned_groups = brewery_df.groupby('IsReturned')
Returned_df = Returned_groups[['Volume']].count()
Returned_df['%% volume'] = (Returned_df.Volume / 36282) * 100
Returned_df


# In[51]:


mylabels = ["N", "Y"]

fig1, ax1 = plt.subplots()
ax1.pie(Returned_df.Volume, labels = mylabels);
plt.legend()
plt.title('Percentage Volume Returned');
st.pyplot(fig1)


# In[35]:


#Question 4
st.write('Question 4')

img = Image.open("./image/19.png")
st.image(img)

Truck_Cat_groups = brewery_df.groupby('Truck_CAT')
Truck_Cat_df = Truck_Cat_groups[['Volume']].count()
Truck_Cat_df


# In[52]:


st.bar_chart(Truck_Cat_df)


# In[37]:


#Question 5
st.write('Question 5')

img = Image.open("./image/20.png")
st.image(img)

Type_load_groups = brewery_df.groupby('Typeload')
Load_Type_df = Type_load_groups[['Volume']].count()
Load_Type_df


# In[53]:


st.bar_chart(Load_Type_df)


# In[39]:


#Question 6
st.write('Question 6')

img = Image.open("./image/21.png")
st.image(img)

Month_volume_groups = brewery_df.groupby('Site')
Depot_volume_df = Month_volume_groups[['Volume']].sum()
Depot_volume_df


# In[54]:


st.bar_chart(Depot_volume_df)

st.header('INSIGHTS')
st.text('From the above we could gather the following...')
st.markdown('* **1.** It was discovered that the trucks of size 10p moved higher volume of products this could be decribed as more work and engagements from drivers and logistics manager in this section.')
st.markdown('* **2.** It was also great to know that the highest production month was March with a drastic reduction in the month of May and June, this could be as a result of social factors (the Muslim fasting period). With this, the planning manager is able to put things in place to cushion this effect.')
st.markdown('* **3.** More volume of products were returned, this could be based on several factors and should be looked into to reduce the return rate drastically.')
st.markdown('* **4.** More trucks could be purchased as Hired trucks are seen to do most of the supply, with this expenses could be cut short over time.')
st.markdown('* **5.** It was observed the the Gateway depot produced the hihest volume followed by onitsha, this could be as a result of presence of more hands, bigger and more sophisticated machineries amongst other things, depots like abuja, Makurdi and the likes with little production should be looked into so as to tap into their full potentials.')


url = 'To view more of my projects and connect with me, kindly click [Here](https://letters-of-michael.github.io/Oluwaseyi-Michael.github.io/)'
st.markdown(url, unsafe_allow_html=True)

urlp = 'To view my portfolio and contact me, please click  [Portfolio](https://letters-of-michael.github.io/Oluwaseyi-Michael.github.io/)'
st.markdown(urlp,unsafe_allow_html=True)



st.write('By Oluwaseyi-Michael')












