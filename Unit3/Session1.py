# Problem 1
# def count_mississippi(limit):
#   for num in range(1, limit):
#     print( f"{num} mississippi")

# count_mississippi(5)

'''Problem 2: Swap Ends
Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.'''

'''
U: flip the first and the last letter of a word

Edge cases:
-What if the word has 1 letter
-What if it is an empty str
-General case - str has multiple letters

P: 
-accessing letters like list elements
-if word has less than 
'''


# def func(str):
#   if len(str) < 1:
#     print(str)

#   first = str[0]
#   last= str[-1]
#   between=str[1:-1:]
#   new= last + between + first
#   return new

# str = "boat"
# swapped = func(str)
# print(swapped)


'''
Problem 3: Is Pangram
Write a function is_pangram() that takes in a string my_str as a parameter and returns True if the string is a pangram and False if not. A pangram is a sentence containing every letter in the English alphabet.
'''
'''
U: 
-if str is a pangram -> true
-if str not pangram -> false


'''


# import string
# def is_pangram(my_str):
#   alphabets=string.ascii_lowercase
#   for i in alphabets:
#     if i not in my_str:
#       return False
#   return True

# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))

'''Problem 4: Reverse String
Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.'''

'''
U: return a reverse string
P:
- def func(str)
- new = str[::-1]
'''

# def reverse_string(my_str):
#   new= my_str[::-1]
#   return new

# my_str = "live"
# print(reverse_string(my_str))

'''Write a function first_unique_char() that given a string my_str as a parameter, it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.
U: return the index of the first character that is unigue in the string
P: 
- def first_unigue_char(my_str)
default = -1
for i in my_str:
  for j in my_str:
    if j != i
    return my_str[i]
    else return default



  str[0]
  for i in str:
   if i != str[0]
    return str[i]
'''
# def first_unigue_char(my_str):

#   for i in my_str:
#     for j in my_str:
#       if i != j:
#         return my_str[i]
#       else:
#         return -1


# my_str = "leetcode"
# print(first_unigue_char(my_str))

# str2 = "loveleetcode"
# print(first_unigue_char(str2))

# str3 = "aabb"
# print(first_unigue_char(str3))



# Solution 2
# def first_unique_char(my_str):
#   # if not my_str:  
#   #     return -1

#   for i in range(len(my_str)):
#       char = my_str[i]
#       if my_str.count(char) == 1:
#           return i

#   return -1

# # Example usage
# print(first_unique_char("leetcode"))  # Output: 0
# print(first_unique_char("loveleetcode"))  # Output: 2
# print(first_unique_char("aabb"))  # Output: -1




'''1) First, create a dictionary to track character occurrences
2) Loop through each character of the input string
  a) Add the character to the dictionary with one occurrence if it's new
  b) Add one to the occurrence of the character in the dictionary
3) Loop through each character of the input string again, but also track the current index
  a) If that character occurs once, return the current index
4) If no character with value 1 is found in the dictionary, return -1'''
#Solution 3
def first_uniq_char(myStr):
  # Count occurrences
  char_count = {}
  for char in myStr:
      if char in char_count:
          char_count[char] += 1
      else:
          char_count[char] = 1

  # Find the first non-repeating character
  for index, char in enumerate(myStr):
      if char_count[char] == 1:
          return index
  return -1