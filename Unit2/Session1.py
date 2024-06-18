'''Problem 2: Create a Dictionary
Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. The function returns a dictionary where each item in keys is paired with a corresponding item in values.

keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). You may assume keys and values are the same length.

'''

'''
Understand: 
- def func with params
- returns a dict where each item in keys is paired with an item in values list
Plan:
Implement
'''

# def func(keys, values):
#   dict={}
#   for i in range(len(keys)):
#     dict[keys[i]]=values[i]
#   return dict

# keys = ["peanut", "dragon", "star", "pop", "space"]
# values = ["butter", "fly", "fish", "corn", "ship"]
# print(func(keys, values))


'''Write a function print_pair() that takes in a dictionary dictionary and a key target as parameters. The function looks for the target and when found, it prints the key and it's associated value as "Key: <key>" followed by "Value: <value>". If target is not in dictionary, print "That pair does not exist!".'''


'''
U:
-search for dict key
-if found it prints the key and value of dict
-if not found prints "Pair doesnt exist"
'''
# def func(dict, target):
#   if target in dict:
#     # print(dict[target]) this is only printing the values
#     print("Key:" + target)
#     print("Values:"+ dict[target])
#   else:
#     print("Pair does not exist")

# dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
# func(dictionary, "patrick")
# func(dictionary, "plankton")
# func(dictionary, "spongebob")

'''
Problem 4: Keys Versus Values
Write a function keys_v_values() that takes in a dictionary dictionary whose keys and values are both integers. The function should find the sum of all keys in the dictionary and the sum of all values.
If the sum of all keys is greater than the sum of all values, the function should return the string "keys".
If the sum of all values is greater than the sum of all keys, the function should return the string "values".
If keys and values have equal sums, the function should return the string "balanced".
'''

''' 
U: 
-def func with dict param
- keys and values both ints
- func -> sum of all keys 
- func -> sum of all values
- if sum of keys >sum of vals
      -return str keys
- if sum of keys< sum of vals
      -return str vals
- if = 
      -return balanced
      
'''

def func(dict):
  sum_keys=sum(dict.keys())  '''prints a list of all keys'''
  sum_vals=sum(dict.values())
  # if sum of keys >sum of vals
  #       -return str keys
  # - if sum of keys< sum of vals
  #       -return str vals
  # - if = 
  #       -return balanced