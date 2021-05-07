#!/usr/bin/env python
# coding: utf-8

# In[17]:


def patterncount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)):
        if(text[i:i+len(pattern)]==pattern):
            count += 1
    return count 


def findClump(genome, k, L, t):   #k is len of k-mer, L is length of genome, t is occurence
    count = {}
    for i in range(L):
        pattern = genome[i:i+k]
        if (patterncount(genome, pattern)==t):
            count[pattern] = patterncount(genome, pattern)
    print(" ".join(count.keys()))    
    return count

print(findClump('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA',5, 50, 4))


# In[ ]:




