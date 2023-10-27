#!/usr/bin/env python
# coding: utf-8

# In[4]:


from pywaffle import Waffle
import matplotlib.pyplot as plt
dept=['cse','ece','mech','chem']
stud=[360,300,150,200]
plt.figure(FigureClass=Waffle,rows=5,values=stud,label=dept)
plt.show()


# In[5]:


get_ipython().system('pip  install pywaffle')


# In[2]:


from pywaffle import Waffle
import matplotlib.pyplot as plt
dept=['cse','ece','mech','chem']
stud=[360,300,150,200]
plt.legend(loc='lower right')
plt.figure(FigureClass=Waffle,rows=5,values=stud,label=dept,columns=20)
plt.show()


# In[16]:


#word cloud for text data
get_ipython().system('pip install wordcloud')


# In[6]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud
txt="we are cse students.cse is best branch they are very good qualifications in faculty our  uha is there "
wc=WordCloud(background_color="pink").generate(txt)
plt.imshow(wc)


# In[9]:


wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(txt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
plt.show()


# In[24]:


get_ipython().system('pip install folium')


# In[11]:


import folium 
mp=folium.Map(location=[16.7,80.8])
mp


# In[28]:


import folium 
mp=folium.Map(location=[16.4,81.7],width=500,height=500,tile='stamen terrain')#latitude and longitude
mp


# In[17]:


import folium 
folium.Marker(location=[16.79,80.8],popup="RGUKT NUZ",tooltip="hello rgukt").add_to(mp)
mp


# In[33]:


import folium

m = folium.Map(location=[16.7,80.5], zoom_start=13, tiles='Stamen Terrain')
folium.TileLayer('Stamen Terrain').add_to(m)
folium.TileLayer('Stamen Toner').add_to(m)
folium.TileLayer('Stamen Watercolor').add_to(m)
folium.TileLayer('cartodbpositron').add_to(m)
folium.TileLayer('cartodbdark_matter').add_to(m)
folium.LayerControl().add_to(m)

m


# In[14]:


import folium
m=folium.Map(location=[16.1,80.8])
m
folium.Marker(location=[16.1,80.8],popup="RGUKT NUZVID").add_to(m)
m


# In[16]:


import folium 
mp=folium.Map(location=[16.7,81.8])
folium.Marker(location=[16.7,81.8],popup="rgukt nuzvid",tooltip="click to see rgukt").add_to(mp)
mp


# In[ ]:




