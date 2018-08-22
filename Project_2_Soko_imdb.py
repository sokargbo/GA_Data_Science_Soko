
# coding: utf-8

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">
# 
# # Project 2: Analyzing IMDb Data
# 
# _Author: Kevin Markham (DC)_
# 
# ---

# For project two, you will complete a serious of exercises exploring movie rating data from IMDb.
# 
# For these exercises, you will be conducting basic exploratory data analysis on IMDB's movie data, looking to answer such questions as:
# 
# What is the average rating per genre?
# How many different actors are in a movie?
# 
# This process will help you practice your data analysis skills while becoming comfortable with Pandas.

# ## Basic level

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# #### Read in 'imdb_1000.csv' and store it in a DataFrame named movies.

# In[2]:


movies = pd.read_csv('./data/imdb_1000.csv')
movies.head()


# #### Check the number of rows and columns.

# In[3]:


movies.shape


# In[5]:


movies.ndim


# #### Check the data type of each column.

# In[10]:


movies.dtypes


# #### Calculate the average movie duration.

# In[12]:


movies.duration.mean()


# #### Sort the DataFrame by duration to find the shortest and longest movies.

# In[25]:



movies.duration.head(1)


# In[26]:


movies.duration.tail(1)


# #### Create a histogram of duration, choosing an "appropriate" number of bins.

# In[35]:


movies.duration.hist();


# In[39]:


movies.duration.plot(kind='hist', bins=15);


# #### Use a box plot to display that same data.

# In[38]:


movies.duration.plot(kind='box');


# ## Intermediate level

# #### Count how many movies have each of the content ratings.

# In[47]:


#movies.content_rating.star_rating.counts()?
movies.content_rating.value_counts()


# #### Use a visualization to display that same data, including a title and x and y labels.

# In[51]:


movies.content_rating.value_counts().plot(kind='bar', title='Top Movies by Content Rating')
plt.xlabel('Content Rating')
plt.ylabel('Number of Movies')


# #### Convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP.

# In[53]:


movies.content_rating.replace(['NOT RATED', 'APPROVED', 'PASSED', 'GP'], 'UNRATED', inplace=True)


# #### Convert the following content ratings to "NC-17": X, TV-MA.

# In[54]:


movies.content_rating.replace(['X', 'TV-MA'], 'NC-17', inplace=True)


# #### Count the number of missing values in each column.

# In[59]:


movies.isnull().sum()


# #### If there are missing values: examine them, then fill them in with "reasonable" values.

# In[60]:


movies.content_rating.replace(['null'], '5', inplace=True)


# In[61]:


#Alternative...?
movies[movies.content_rating.isnull()]
movies.content_rating.fillna('UNRATED', inplace=True)


# #### Calculate the average star rating for movies 2 hours or longer, and compare that with the average star rating for movies shorter than 2 hours.

# In[67]:


movies[movies.duration >= 120].star_rating.mean()


# In[66]:


movies[movies.duration < 120].star_rating.mean()


# #### Use a visualization to detect whether there is a relationship between duration and star rating.

# In[72]:


movies.plot(kind='scatter', x='duration', y='star_rating', alpha=0.2);


# #### Calculate the average duration for each genre.

# In[93]:


movies.groupby('genre').duration.mean()


# ## Advanced level

# #### Visualize the relationship between content rating and duration.

# In[95]:


movies.boxplot(column='duration', by='content_rating')
movies.hist(column='duration', by='content_rating', sharex=True);


# #### Determine the top rated movie (by star rating) for each genre.

# In[96]:


movies.groupby('genre').title.first()


# #### Check if there are multiple movies with the same title, and if so, determine if they are actually duplicates.

# In[102]:


dupe_titles = movies[movies.title.duplicated()].title
movies[movies.title.isin(dupe_titles)]


# #### Calculate the average star rating for each genre, but only include genres with at least 10 movies
# 

# #### Option 1: manually create a list of relevant genres, then filter using that list

# In[ ]:


# Answer:


# #### Option 2: automatically create a list of relevant genres by saving the value_counts and then filtering

# In[ ]:


# Answer:


# #### Option 3: calculate the average star rating for all genres, then filter using a boolean Series

# In[ ]:


# Answer:


# #### Option 4: aggregate by count and mean, then filter using the count

# In[103]:


genre_ratings = movies.groupby('genre').star_rating.agg(['count', 'mean'])
genre_ratings[genre_ratings['count'] >= 10]


# ## Bonus

# #### Figure out something "interesting" using the actors data!

# In[135]:


actors=movies.groupby('actors_list').title.first()

