#!/usr/bin/env python
# coding: utf-8

# In[9]:


pattern_O = 'TTTCCCTAC'
d = 2
dict_of_variation = {}
base_pair = 'A','T','C','G'
def Neighbors (pattern, d):
    working_pattern = pattern
    for i in range(len(pattern)):
        prefix = pattern[0:i]
        suffix = pattern[i+1:len(pattern)]
        for b in base_pair:
            working_pattern = prefix+b+suffix
            if HammingDistance (pattern_O, working_pattern) <= d:
                if working_pattern in dict_of_variation:
                    pass
                else:
                    dict_of_variation[working_pattern]=+1
                    Neighbors(working_pattern, d)
    return (dict_of_variation)

def HammingDistance(p, q):

   count = 0

   for i in range(len(p)):
       x = p[i]
       y = q[i]
       if x != y:
           count = count + 1
   return count          

print (*Neighbors (pattern_O, d))


# In[ ]:




