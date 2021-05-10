#!/usr/bin/env python
# coding: utf-8

# In[1]:


pattern = "GAGCCACCGCGATA"


def gc_skew(pattern):

    skew = 0

    print(skew, end=" ")

 

    for nu in pattern:

        if nu == "C":

            skew -= 1

        elif nu == "G":

            skew += 1

 

        print(skew, end=" ")


 

gc_skew(pattern)


# In[ ]:




