#!/usr/bin/env python
# coding: utf-8

# In[8]:


def FrequencyMap (text,k):
    freq = {}
    n=len(text)
    for i in range (n-k+1):
        Pattern = text [i:i+k]
        if Pattern not in freq:
            freq[Pattern] = 1
        else: freq[Pattern] +=1
    return freq

freq = FrequencyMap('GTGTAAAGCGGATGCCCAGTAAAGCGATAAAGCGTAAAGCGTGGTGGCTAAAGCGTTAAAGCGTAAAGCGATAAAGCGTAGAGTCTAAAGCGCCTAAAGCGCCGTATAAAGCGTAGTAAAGCGTAGTCCACTCGTAAAGCGGTTAAAGCGTTAAAGCGTAAAGCGTAAAGCGATAAAGCGTTAAAGCGCTAAAGCGTTAAAGCGGCTTCTAAAGCGAACTAAAGCGCCAACTGTAAAGCGGGAGCTAAAGCGTAAAGCGTACGCGCTAAAGCGTAAAGCGAGGCCCAGTAAAGCGCGGAGCTAAAGCGCTTTAAAGCGCAGGACTTGGGTAAAGCGCTAAAGCGTAAAGCGTTCAGCTCATTAAAGCGCTAAAGCGTAAAGCGAAAATCGTAAAGCGAGCTAAAGCGTAAAGCGTAAAGCGCTGGTAAAGCGTTAAAGCGTTAAAGCGCCCGTAAAGCGCGCTAAAGCGTTTAAAGCGTGTGCTGACTTAAAGCGGACATACTTAAAGCGCAATAAAGCGTAAAGCGTTAAAGCGCATTAAAGCGGCTAAAGCGGTAAAGCGTTGGTTGCATAAAGCGTTTAAAGCGGTAAAGCGTAAAGCGTAAAGCGTTAAAGCGTAAAGCGTAAAGCGCAAAACTTGCTAAAGCGACGTAAAGCGTAAAGCGGAGTAATAAAGCGTTTTAAAGCGAACGATAAAGCGTAAAGCGTTTCGCTAAAGCGAATAAAGCGTAAAGCGTCGTGTAAAGCGCTTAAAGCGTGGTAAAGCGTGTTAAAGCGCGTAAAGCGGACTGGCGTAAAGCGTAAAGCGTTAAAGCGTAAAGCGCGTAAAGCGACTAAAGCGACCCGTAAAGCGAAATCACCGCTGGTAAAGCGGATCATTTAAAGCGTAAAGCGTTAAAGCGTCAGCTAAAGCGCCGGAATGCAAGTTAAAGCGTAAAGCGTAAAGCGCCGTAAAGCGTAAAGCGTGCTAAAGCGGTTTAAAGCGTCGCTAAAGCGTAAAGCGTGGGTAAAGCG',11)

max=0
for i in freq:
    no = freq[i]
    if no>max:
        max=no
        res=i
print (" Most frequent number is:" + (res))


# In[ ]:




