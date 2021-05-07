#!/usr/bin/env python
# coding: utf-8

# In[16]:


Pattern = 'ATAT'
Genome = 'GATATTTGATATATATT'
Position = []
for i in range(len(Genome) - len(Pattern)+1):
    if Genome[i:i + len(Pattern)] == Pattern:
        Position.append(i)
print(*Position)


# In[ ]:




