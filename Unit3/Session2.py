'''
Problem 1: Sum of Strings
Write a function sum_of_number_strings() that takes in a list of strings nums. Each string is a representations of integers. The function should return the sum of these strings as an integer.'''

'''
- def func(str)
  total= 0
  for i in str: 
   int(i)
  sum = total +=
  return sum
  str=["10","20"]
   
'''
# def func(nums):
#   total= 0
#   for i in nums: 
#    new_int= int(i)
#    total += new_int
#   return total

# nums = ["10", "20", "30"]
# sum = func(nums)
# print(sum)


'''Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes all duplicates in the list. The function returns the modified list.'''

'''
- def func(nums)
- new_nums=[] create a new list that we append the nums elements to it,
 we compare elements between the two

'''
# def func(nums):
#   new_nums=[]
#   for i in nums:
#    if i not in new_nums:
#     new_nums.append(i)
#   return new_nums

# nums = [1,1,1,2,3,4,4,5,6,6,7,7,8]
# print(func(nums))  

'''Problem 3: Reverse Letters
Write a function reverse_only_letters() that takes in a string s as a parameter. The function reverses the order of the letters in the string and returns the new string. Non-letter characters should remain in their original positions.'''

'''
-def func(s)
  - reverse letter order - slicing
  - retrun new reversed str

  - if letter not char
  - does not change position


edge case maybe: keep in mind capitalization
'''
# Try 1
'''import string
def func(s):
  
  chars=string.ascii_lowercase
  for i in s:
    if i not in chars:
      return 1
    else:
      reversed_str= s[::-1]
      return reversed_str
      

s = "a-bC-dEf-ghIj"
reversed_s = func(s)
print(reversed_s)'''

#try 2 with AI guidance
import string
def func(s):
  letters=[]
  non_letters=[]
  alphabet = string.ascii_letters

  for char in s:
    if char not in alphabet:
      non_letters.append(char)
    else:
      letters.append(char)

  reversed_letters= letters[::-1]
  reversed_str = "".join(reversed_letters) + "".join(non_letters) 
  return reversed_str


s = "a-bC-dEf-ghIj"
reversed_s = func(s)
print(reversed_s)