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

def func(keys, values):
  dict={}
  for i in range(len(keys)):
    dict[keys[i]]=values[i]
  return dict

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(func(keys, values))