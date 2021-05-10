#!/usr/bin/env python
# coding: utf-8

# In[23]:


dist = 0

p='GGGCCGTTGGT'
q='GGACCGTTGAC'
for i in range(len(p)):
    if p[i] != q[i]:
        dist += 1
print(dist)


# In[ ]:




