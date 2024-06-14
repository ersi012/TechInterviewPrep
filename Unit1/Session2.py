#p3
#U: func returns a new list of doubled nums
def doubled(lst):
  new_lst=[]
  for i in lst:
    new_lst.append(i*2)
  return new_lst

print(doubled([1,2,3]))