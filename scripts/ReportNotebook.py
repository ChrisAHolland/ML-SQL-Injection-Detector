#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[6]:


burp = [99.84, 99.84]
OWASP = [99.40, 99.85]
FuzzDB = [99.69, 99.84]

plt.plot(burp, label="Kali Linux Burp Suite")
plt.plot(OWASP, label="OWASP JBroFuzz")
plt.plot(FuzzDB, label="FuzzDB")
plt.legend()
plt.show()


# In[7]:


burp = [99.84, 99.84, 99.923]
OWASP = [99.40, 99.85, 99.925]
FuzzDB = [99.69, 99.84, 99.924]

plt.plot(burp, label="Kali Linux Burp Suite")
plt.plot(OWASP, label="OWASP JBroFuzz")
plt.plot(FuzzDB, label="FuzzDB")
plt.legend()
plt.show()


# In[8]:


x = np.arange(3)
plt.bar(x, height= [0.75,0.625,0.5])
plt.xticks(x, ['FuzzDB','OWASP','Burp Suite'])
plt.ylabel("Accuracy")


# In[ ]:




