'''Problem 1: Cast Vote
Write a function cast_vote() that records a vote for a candidate in an election. The function accepts a dictionary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.'''


'''
U:
-def func

# '''

# def func(votes, candidate):
#   if candidate in votes:
#     votes[candidate]+= 1
#   else:
#     votes[candidate]= 1
#   return votes

# votes = {"Alice": 5, "Bob": 3}
# func(votes, "Alice")
# print(votes)
# func(votes, "Gina")
# print(votes)

'''
Problem 2: Keys in Common
Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common to both dictionaries. The function returns a list of common keys.
'''

# def func(dict1, dict2):
#   keys1=dict1.keys()
#   keys2=dict2.keys()

#   common_keys=[]
#   for i in keys1:
#     if i in keys2[i]:
#       common_keys.append(i)
    
#   return common_keys

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_keys = func(dict1, dict2)
# print(common_keys)




"""
Problem 5: Find Majority Element

Write a function find_majority_element() that takes in a list of integers elements and finds the majority element in the list. 

A majority element is an element that appears more than n/2 times where n is the size of the list. 

If there is no majority element, return None.

def find_majority_element(elements):
    pass
Example Usage:

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
Example Output: 2
"""
"""
Understand:
- def func with param list 
-Find the most frequent element list
  x=  len(lst)/2
- for i in lst
- if i > x
- return i
-else 
- return None

Implement:

Plan:

"""

# WRONG SOLUTION

# def find_majority_element(elements):
#   x = len(elements) / 2
#   for i in elements:
#     if i > x:
#       return i
#     else:
#       return None


# elements = [2, 2, 1, 1, 1, 2, 2]
# print(find_majority_element(elements))
