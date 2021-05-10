#!/usr/bin/env python
# coding: utf-8

# In[2]:


dist = 0

p='TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
q='GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'
for i in range(len(p)):
    if p[i] != q[i]:
        dist += 1
print(dist)


# In[3]:


def min_skew(dna_seq):
    #finds DNA pos where skew is min (i.e OriC)
    
    skew_dic = {0:0}
    
    import numpy as np
    for i, nuc in enumerate(dna_seq):
        
        if nuc == 'C': skew_dic.update({i+1: list(skew_dic.values())[-1] - 1})
        if nuc == 'G': skew_dic.update({i+1: list(skew_dic.values())[-1] + 1})
        if nuc == 'A': skew_dic.update({i+1: list(skew_dic.values())[-1] + 0})
        if nuc == 'T': skew_dic.update({i+1: list(skew_dic.values())[-1] + 0})
        
    # Find item with min value in Dictionary
    min_val = min(skew_dic.items(), key = lambda x: x[1])
    
    # Find all items with the min value
    min_vals = [key for key,value in skew_dic.items() if value == min_val[1]]
    
    return min_vals

print(min_skew('GATACACTTCCCGAGTAGGTACTG'))


# In[4]:


pattern=input("Pattern=")
text=input("Text=")
d=input("d=")

def hd(str1,str2):
    i=0
    count=0
    while(i<len(str1)):
        if(str1[i]!=str2[i]):
            count +=1
        i +=1
    return count

def apm(pattern,text,d):
    count=0
    for i in range (len(text)-len(pattern)+1):
        if hd(pattern,text[i:i+len(pattern)])<=int(d):
            count+=1
    return count

print(apm(pattern,text,d))


# In[9]:


pattern_O = 'TGCAT'
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

count=0
for i in dict_of_variation:
    count+=1
print(count)


# In[ ]:




