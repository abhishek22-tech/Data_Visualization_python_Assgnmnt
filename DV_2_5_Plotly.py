#!/usr/bin/env python
# coding: utf-8

# In[11]:


import plotly.graph_objs as go
import numpy as np
x = np.random.randn(2000)
y = np.random.randn(2000)
iplot([go.Histogram2dContour(x=x, y=y,
contours=dict (coloring='heatmap')),
go.Scatter(x=x, y=y, mode='markers',
marker=dict(color='white', size=3,
opacity= opacity=0.3))], show_link=False)


# In[10]:


import plotly.offline as offline
import plotly.graph_objs as go
offline.plot({'data': [{'y': [14, 22, 30,
44]}], 'layout': {'title': 'Offline Plotly', 'font':
 dict(size=16)}}, image='png')


# In[16]:


from plotly import __version__
from plotly.offline import download_plotlyjs,
init_notebook_mode, plot, iplot init_notebook_mode(connected=True)
print (__version__)
import plotly.graph_objs as go
plot([go.Scatter(x=[95, 77, 84], y=[75, 67, 56])])


# In[15]:





# In[ ]:




