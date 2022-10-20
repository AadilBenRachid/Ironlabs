#!/usr/bin/env python
# coding: utf-8

# ### Kata 1 Remove All The Marked Elements of a List

# In[ ]:


class List:
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if i not in values_list]


# ### Kata 2 Method For Counting Total Occurence Of Specific Digits

# In[3]:


class List(object):
    @staticmethod
    def count_spec_digits(integers_list, digits_list):
        result = []
        str_list = ''.join(str(i) for i in integers_list)
        for digit in digits_list:
            result.append((digit, str_list.count(str(digit))))
        return result


# ### Kata 3 Ordered Count of Characters

# In[4]:


from collections import Counter

def ordered_count(input):
    return list(Counter(input).items())

