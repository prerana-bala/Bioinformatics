#!/usr/bin/env python
# coding: utf-8

# In[ ]:


d=open("Salmonella_enterica.txt").readlines()

#remove the header
d=d[1:-1]
print minimumSkew("".join(map(str.strip, d)))
#[3764856, 3764858]

def strip1(t):
  return  t.rstrip("\n")
print minimumSkew("".join(map(strip1, d)))
#[3818639, 3818641]

def strip2(t):
  return  t.rstrip("\r\n")
print minimumSkew("".join(map(strip2, d)))

