#!/usr/bin/env python
# coding: utf-8

# # Problem 1
# 
# Complete the function below, which takes arguments `a` and `b` and you can assume they will be integer numbers.  The function should test whether `a` is evenly divisable by `b`.  If it is evenly divisable, it should return a string that reads
# 
# ```
# "a is evenly divisible by b!"
# ```
# 
# Please note that `a` and `b` should be replaced with their actual values given in the function call.  In the event that `a` is not evenly divisable by `b`, the function should store a return
# 
# ```
# "a is not evenly divisible by b. The remainder is c."
# ```
# 
# where `c` is the remainder.  Again, `a`, `b`, and `c` should be replaced by thier actual values in the function call.  For example, calling the function with
# 
# ```python
# is_evenly_divisible(4, 2)
# ```
# 
# should return
# 
# ```python
# "4 is evenly divisible by 2!"
# ```
# 
# and calling the function with
# 
# ```python
# is_evenly_divisible(5, 3)
# ```
# 
# should return
# 
# ```python
# "5 is not evenly divisible by 3. The remainder is 2."
# ```

# In[1]:


def is_evenly_divisible(a, b):
    if a % b == 0:
        return f"{a} is evenly divisible by {b}!"
    else:
        remainder = a % b
        return f"{a} is not evenly divisible by {b}. The remainder is {remainder}."


# In[3]:


is_evenly_divisible(10, 2)


# In[4]:


is_evenly_divisible(10,3)



# In[2]:


# Test cases
print(is_evenly_divisible(4, 2))
print(is_evenly_divisible(5, 3))


# # Problem 2
# 
# Complete the function below. Assume the arguments `a` and `b` are integer or floating point numbers.  The argument `operation` is a string that has one of the following values exactly: `'add', 'subtract', 'multiply', 'divide'`.
# 
# Given one of those values for `operation`, design a series of tests that will return the cooresponding mathematical operation for the numbers defined in `a` and `b`.  So if `operation = 'add` then you should return the sum of `a` and `b`.  Likewise for the other operations.  In the event that the user inputs in invalid value for `operation`, have the function return the string:
# 
# ```
# 'Operation must be one of: ["add", "subtract", "multiply", "divide"]'
# ```
# 
# This string has been placed in a comment below for your assistance.  The following examples should clarify the desired implementation of the function.  If the function is called with
# 
# ```python
# math_operation(4, 2, 'add')
# ```
# 
# will return `6`.
# 
# ```python
# math_operation(4, 2, 'multiply')
# ```
# 
# will return `8`.
# 
# ```python
# math_operation(4, 2, 'divide')
# ```
# 
# will return `2`.
# 
# ```python
# math_operation(4, 2, 'plus')
# ```
# 
# will return `'Operation must be one of: ["add", "subtract", "multiply", "divide"]'`.

# In[5]:


def math_operation(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        return 'Operation must be one of: ["add", "subtract", "multiply", "divide"]'


# In[6]:


# Test cases
print(math_operation(4, 2, 'add'))
print(math_operation(4, 2, 'subtract'))
print(math_operation(4, 2, 'multiply'))
print(math_operation(4, 2, 'divide'))
print(math_operation(4, 2, 'plus'))

