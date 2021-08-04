#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([2,3,6]))


# In[ ]:


#Question 2
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# In[ ]:


#Question 3
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)


# In[ ]:


#Question 4
 number = 8

numberDict = {}
for i in range(1, number+1):
    numberDict[i] = i*i

print(numberDict)


# In[ ]:


#Question 5
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))

