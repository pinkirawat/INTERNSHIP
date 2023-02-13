#!/usr/bin/env python
# coding: utf-8

# # Write a python program to display IMDB’s Top rated 50 movies’ data (i.e. name, rating, year of release)
# and make data frame

# In[189]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[190]:


from bs4 import BeautifulSoup
import requests


# In[191]:


url='https://www.imdb.com/search/title/?groups=top_100'


# In[192]:


IMBD=requests.get(url)


# In[193]:


soup=BeautifulSoup(IMBD.content)


# In[194]:


movie_names = [i.text.split('\n')[2]  for i in soup.find_all(class_="lister-item-header")]

    
    
movie_names    


# In[195]:


rating=[i.text.strip() for i in soup.find_all(class_="inline-block ratings-imdb-rating")]


# In[196]:


rating


# In[197]:


release_year = []
for i in soup.find_all(class_="lister-item-year text-muted unbold"):
    release_year.append(i.text)


# In[198]:


release_year


# In[199]:


import pandas as pd
df=pd.DataFrame({'Movies':movie_names,'Ratings':rating,'Release_Year':release_year})

df


# In[ ]:





# In[ ]:





# In[ ]:





# # Write a python program to display IMDB’s Top rated 50 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.

# In[47]:


url='https://www.imdb.com/india/top-rated-indian-movies/'


# In[48]:


IMBD=requests.get(url)


# In[49]:


soup=BeautifulSoup(IMBD.content)


# In[64]:


movie_name=[i.text.split('\n')[2] for i in soup.find_all(class_="titleColumn")]


# In[54]:


movie_name


# In[55]:


rating=[i.text.strip() for i in soup.find_all(class_="ratingColumn imdbRating")]

rating


# In[56]:


release_year=[]
for i in soup.find_all(class_="secondaryInfo"):
    release_year.append(i.text)


# In[57]:


release_year


# In[67]:


df=pd.DataFrame({'Movie':movie_name,'Rating':rating,'Release_Year':release_year})

df


# In[ ]:





# # Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice)
# from https://presidentofindia.nic.in/former-presidents.htm and make data frame.

# In[68]:


url='https://presidentofindia.nic.in/former-presidents.htm'


# In[69]:


POI=requests.get(url)


# In[70]:


soup=BeautifulSoup(POI.content)


# In[81]:


name=[i.text.split('\n')[1] for i in soup.find_all(class_="presidentListing")]


name


# In[93]:


term_of_office=[i.text.split('\n')[2] for i in soup.find_all(class_="presidentListing")]

term_of_office
  


# In[95]:


df=pd.DataFrame({'Name':name,'Term_Of_Office':term_of_office})


df


# # Write a python program to scrape mentioned details from dineout.co.in and make data frame

# # i) Restaurant name

# # ii) Cuisine

# # iii) Location

# # iv) Ratings

# # v) Image URL

# In[204]:


URL=('https://www.dineout.co.in/delhi-restaurants/welcome-back')


# In[205]:


DINEOUT=requests.get(URL)


# In[206]:


soup=BeautifulSoup(DINEOUT.content)


# In[207]:


title=[]
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    title.append(i.text)

    
title    


# In[208]:


location=[]
for i in soup.find_all('div', class_="restnt-loc ellipsis"):
    location.append(i.text)
    
    
location   


# In[209]:


rating=[]
for i in soup.find_all(class_="restnt-rating rating-4"):
    rating.append(i.text)
    
    
rating    


# In[210]:


image=[]
for i in soup.find_all('img', class_="no-img"):
    image.append(i.get('data-src'))
    
    
image    


# In[211]:


cuisines=[]
for i in soup.find_all('h4',class_="collapsed"):
    cuisines.append(i.text)
    
    
cuisines    


# In[212]:


df=pd.DataFrame({'Name':title,'Location':location,'Rating':rating,'Image':image})

df


# # Write a python program to scrape the details of most downloaded articles from AI in last 90
# days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details and make data framei) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL

# In[ ]:





# In[247]:


URL=('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[248]:


JOUR=requests.get(URL)


# In[249]:


soup=BeautifulSoup(JOUR.content)


# In[250]:


title=[]
for i in soup.find_all('h2' ,class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    title.append(i.text)
    
    
title    


# In[251]:


authors=[i.text.split()[0]  for i in soup.find_all('p', class_="sc-1thf9ly-0 sc-1thf9ly-1 iwnLUR fXmEge")]
authors.append(i.text)
    
    
    
authors    


# In[252]:


publish_date=[]
for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    publish_date.append(i.text)
    
    
publish_date    


# In[316]:


df=pd.DataFrame({'Title':title,'Authors':authors,'Published_Date':publish_date})

df


# In[ ]:





# # Write a python program to display all the header tags from wikipedia.org and make data frame.

# In[260]:


URL=('https://www.wikipedia.org/')


# In[261]:


HD=requests.get(URL)


# In[262]:


soup=BeautifulSoup(HD.content)


# In[243]:


header=[i.text.split()[0]  for i in soup.find_all('div',class_="other-project-text")]
header.append(i.text)
    
header    


# In[244]:


df=pd.DataFrame({'Header':header})

df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


2


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




