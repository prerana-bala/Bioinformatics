#!/usr/bin/env python
# coding: utf-8

# In[33]:


pattern=input("Pattern=")
text=input("Text=")
d=input("d=")

def hd(q,p):
    dist=0
    for i in range(len(p)):
        if(p[i]!=q[i]):
            dist +=1
    return dist

def approx_pat(pattern,text,d):
    positions=[]
    for i in range (len(text)-len(pattern)+1):
        if hd(pattern,text[i:i+len(pattern)])<=int(d):
            positions.append(i)
    return positions

print(*approx_pat(pattern,text,d))


# In[ ]:




