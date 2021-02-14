#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Import splinter and beautifulsoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[2]:


# Setting up a path for a Windows user
executable_path = {'executable_path': 'C:/chromedriver/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

#Optional delay for loading the page
browser.is_element_present_by_css('ul.item_list li.slide', wait_time=1)


# In[5]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[6]:


slide_elem.find('div', class_='content_title')


# In[9]:


# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[10]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[14]:


executable_path = {'executable_path': 'C:/chromedriver/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[15]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[19]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[21]:


# Pare the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[22]:


# Find relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[23]:


# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-spac.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# In[25]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[26]:


df.to_html()


# In[27]:


browser.quit()


# In[ ]:




