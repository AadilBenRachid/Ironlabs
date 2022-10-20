#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json
import requests
import pandas as pd


# In[29]:


response= requests.get('https://xkcd.com/info.0.json')


# In[30]:


response


# In[31]:


results=response.json()


# In[32]:


results


# In[33]:


data=pd.DataFrame(response)
data.head()


# In[10]:


results=response.json()
flattened_data=pd.json_normalize(results)


# In[34]:


flattened_data


# ## Challenge 1: Get a Picture
# #### 1.Go to the link https://xkcd.com
# #### 2.check the headers
# #### 3. check the headers "Expires" value
# #### 4.Provide all HTML codes
# #### 5. Choose the random picture from the website
# #### 6.Get it via API
# #### 7.Save it to your computer

# In[35]:



response.headers


# In[ ]:





# In[36]:


response.headers['Expires']


# 'Expires': 'Fri, 14 Oct 2022 16:26:47 GMT'

# In[37]:


response.content


# In[16]:


html=requests.get('https://xkcd.com/')


# In[18]:


html.text


# In[38]:


response1=requests.get('https://imgs.xkcd.com/comics/2045.png')
response1


# In[47]:


file = open("xkcd.png", "wb")
file.write(response1.content)
file.close()


# ## Challenge 2: Get a password
# #### 1.Go to the https://httpbin.org/get. it is a simple HTTP libraries use for testing
# #### 2.View url
# #### 3.Add parameters to the request 'things':2,'total':25
# #### 4.Add username and password as parameters
# #### 5.Export username and password as dictionary

# In[72]:


response = requests.get('https://httpbin.org/get',{'things':2,'total':25})


# In[73]:


response.url


# In[74]:


r3= requests.get('https://httpbin.org/get',{'things':2,'total':25})
r3


# In[75]:


r3.json()["args"]


# In[78]:


r4= requests.get('https://httpbin.org/get',{'username': 'Aadil','password': 'ben'})
r4


# In[82]:


r4.json()


# In[80]:


r5= requests.post('https://httpbin.org/post',{'username': '...','password': '..'})
r5


# In[81]:


r5.json()


# ## Challenge 3: Hidden Cold Joke

# In[85]:


response=requests.get('https://api.github.com/search/code?q=.scavengerhunt+in:path+repo:ironhack-datalabs/scavenger')
response


# In[86]:


response.json()


# In[92]:


response = requests.get('https://api.github.com/search/code?q=.scavengerhunt in:path+repo:ironhack-datalabs/scavenger');
search = response.json()
search


# In[101]:


files = search['items'];
files = sorted(files, key=lambda file: file['name']);
print(files)


# In[96]:


contents_list = []
headers = {'Accept': 'application/vnd.github.v3.raw', };
headers


# In[97]:


for file in files:
    content_path = ('https://api.github.com/repos/ironhack-datalabs/scavenger/contents/{}').format(file['path']);
    response = requests.get(content_path, headers=headers);
    contents_list.append(response.text);
    
    print(contents_list)


# In[99]:


clean_contents = [word.strip('\n') for word in contents_list]
joke = " ".join(clean_contents);


# In[100]:


joke


# In[ ]:




