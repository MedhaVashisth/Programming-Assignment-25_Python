#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_three(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))


# In[2]:


# Python code to convert dictionary into list of tuples

# Initialization of dictionary
dict = { 'Geeks': 10, 'for': 12, 'Geek': 31 }

# Converting into list of tuple
list = [(k, v) for k, v in dict.items()]

# Printing list of tuple
print(list)


# In[3]:


Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)


# In[4]:


# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)


# In[5]:


# Function to Replace each vowel in
# the string with a specified character
def replaceVowelsWithK(test_str, K):

	# string of vowels
	vowels = 'AEIOUaeiou'

	# iterating to check vowels in string
	for ele in vowels:

		# replacing vowel with the specified character
		test_str = test_str.replace(ele, K)

	return test_str



# Driver Code
# input string
input_str = "Geeks for Geeks"

# specified character
K = "#"

# printing input
print("Given String:", input_str)
print("Given Specified Character:", K)

# printing output
print("After replacing vowels with the specified character:",
	replaceVowelsWithK(input_str, K))


# In[7]:


# Python3 code to demonstrate working of
# Alternate cases in String
# Using list comprehension

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + str(test_str))

# Using list comprehension
# Alternate cases in String
res = [ele.upper() if not idx % 2 else ele.lower() for idx, ele in enumerate(test_str)]
res = "".join(res)

# printing result
print("The alternate case string is : " + str(res))


# In[ ]:




