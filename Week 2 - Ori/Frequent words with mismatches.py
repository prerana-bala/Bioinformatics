#!/usr/bin/env python
# coding: utf-8

# In[14]:


Text = 'CAGGACCCTAACAGGACCACCCAGGTGATACCCTAATTTTCAGGACCTTTTCTAACAGGTTTTACCCTAATGATTTTTTTTTACCTGATACCTGATTTTTTTTTCAGGTGATTTTTTTTTACCACCCTAAACCACCTGATCAGGACCTTTTACCTGATCTAAACCTGATCTAATTTTTTTTTGATCAGGTTTTACCCAGGCAGGTGATTTTTTGATCTAACAGGTGATTTTTCTAATTTTACCACCTTTTTGATCTAACTAATTTTACCACCCTAACTAATTTTTTTTCAGGTTTTCAGGCTAAACCTGATTGATCTAATGATCAGGCAGGACCACCCAGGCAGGCTAACAGGTGATTTTTCTAACTAATGATCTAAACCCTAACAGG'
k = 6
d = 3

def FrequentWordsWithMismatches(Text, k):
    FrequentPatterns = [] 
    Close = {} 
    
    for i in range(0, 4**k): #set up Close array and FrequencyArray with initial values '0'
        Close[i] = 0

    for i in range(0, len(Text)-k+1):
        Neighborhood = Neighbors(Text[i:i+k], d)
        for Pattern in Neighborhood: 
            index = PatternToNumber(Pattern) 
            Close[index] += 1 
    maxCount = max(Close.values())


    for i in range(0, 4**k):
        if Close[i] == maxCount:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates


def remove_duplicates(Text):
    ItemsNoDuplicates = []
    for item in Text:
        if item not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(item)
    return ItemsNoDuplicates


###Hamming Distance###

def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:len(Pattern)+1] == Pattern:
            count += 1
        elif Text[i:len(Pattern)+1] != Pattern:
            if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
                count += 1
    return count

def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

###Hamming Distance###

### Toggle letters of each k-mer  and generate all permutations.

def Neighbors(Pattern, d):
    if d == 0:
        return ([Pattern])
    if len(Pattern) == 1:
        return (['A', 'C', 'G', 'T'])
    Neighborhood = []
    SuffixNeighbors = Neighbors(suffix(Pattern), d)

    for Text in (SuffixNeighbors):
        if HammingDistance(suffix(Pattern), Text) <d:
            for base in "ACGT":
                Neighborhood.append(base + Text)
        else:
            Neighborhood.append(FirstSymbol(Pattern) + Text)
    return (Neighborhood)


def FirstSymbol(Pattern):
    return Pattern[0]

def suffix(Pattern):
    suffix = Pattern[1:len(Pattern)]
    return (suffix)


def PatternToNumber(Pattern):
    prefix = ''
    if Pattern == '':
        return 0
    symbol = Lastsymbol(Pattern)
    prefix = (Prefix(Pattern))
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def Lastsymbol(Pattern):
    return Pattern[-1]

def Prefix(Pattern):
    return Pattern[:len(Pattern)-1]

def SymbolToNumber(symbol):
    if symbol == "A":
        return 0
    elif symbol == "C":
        return 1
    elif symbol == "G":
        return 2
    else:
        return 3


def NumberToPattern(index, k):
    PrefixPattern = ''
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = Quotient(index, 4)
    r = Remainder(index, 4)
    symbol = NumberToSymbol(r)
    PrefixPattern += symbol
    for i in range(k-1):
            r = Remainder(int(prefixIndex), 4)
            symbol = NumberToSymbol(r)
            PrefixPattern += symbol
            prefixIndex = Quotient(int(prefixIndex), 4)
    return reverse(PrefixPattern)

def reverse(text):
    result = ''
    count = len(text) -1
    for x in text:
        result += text[count]
        count -=1
    return result

def NumberToSymbol(r):
    if r == 0:
        return "A"
    elif r == 1:
        return "C"
    elif r == 2:
        return "G"
    else:
        return "T"

def Remainder(num, n):
    return int(num)%n

def Quotient(num, n):
    return int(num)/n

def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

print (' '.join(map(str, (FrequentWordsWithMismatches(Text, k)))))


# In[ ]:




