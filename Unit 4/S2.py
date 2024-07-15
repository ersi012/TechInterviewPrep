'''The two-pointer approach is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. A common variation of this technique is to point one variable at the beginning of one list/string and a second pointer at the beginning of a second list/string, then increment each pointer conditionally to solve a problem.

Using the two pointer approach, write a function merge_sorted_lists() that takes in two sorted lists lst1 and lst2 as parameters and merges them into a single sorted list. The function returns the new list.'''
'''
U:
P:
def func(l1, l2):
  merge_lst=[]
  pointer1= 0
  pointer2= 0

  while pointer1<len(l1) and pointer2<len(l2):
    if l1[pointer1] < l2[pointer2]:
      merge_lst.append(l1[pointer1])
      merge_lst.append(l2[pointer2])
    elif l1[pointer1] > l2[pointer2]:
      merge_lst.append(l2[pointer2])
      merge_list.append(l1[pointer1])  
    else:
     merge_lst.append(l1[pointer1])

    pointer1 += 
    pointer2 = pointer2 + 1 

  return merge_lst



I:'''

# def merge_sorted_lists(l1, l2):
#   merge_lst=[]
#   pointer1= 0
#   pointer2= 0

#   while pointer1<len(l1) and pointer2<len(l2):
#     if l1[pointer1] < l2[pointer2]:
#       merge_lst.append(l1[pointer1])
#       merge_lst.append(l2[pointer2])
#     elif l1[pointer1] > l2[pointer2]:
#       merge_lst.append(l2[pointer2])
#       merge_lst.append(l1[pointer1])
#     else:
#      merge_lst.append(l1[pointer1])

#     pointer1 += 1
#     pointer2 = pointer2 + 1

#   return merge_lst

# lst1 = [1, 3, 5]
# lst2 = [2, 4, 6]
# merged_lst = merge_sorted_lists(lst1, lst2)
# print(merged_lst)
'''Write a function is_subsequence that takes in two strings s and t as parameters and returns True if s is a subsequence of t and False otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some or none of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).'''
'''
U:
- 


- if s is sub of t:
    return True 
  else:
   return False
pointer1= 0 
pointer2 = 0 
if s[pointer1] = t[pointer2]:
  pointer2 +=1
  pointer1 +=1
elif s[pointer1] =! t[pointer2]
  pointer2 = pointer +1
P:
I:'''

# class Solution:
#   def __init__(self, s, t):
#     self.new = self.pointer_logic(s, t)


def is_subsequence(s, t):
  pointer1 = 0
  pointer2 = 0
  while pointer2 < len(t):
    if s[pointer1] == t[pointer2]:
      pointer1 += 1
    pointer2 += 1
    #this part is not necessary
    # elif s[pointer1] != t[pointer2]:
    #   pointer2 = pointer2 +1

# If pointer1 has reached the end of s, all characters of s were found in t
  return pointer1 == len(s)

s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))

s = "cba"
t = "ahbgdc"
print(is_subsequence(s, t))
