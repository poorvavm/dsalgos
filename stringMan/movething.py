def moveThings(list, val_index, new_index):
  for i in range(0, len(list)):
      if i == val_index:
        temp = list[val_index]
        for i in range(val_index, new_index):
          list[i] = list[i+1]
        list[new_index] = temp
  return list

new_list = moveThings(['a','b','c','d','e','f'],2,4)
print new_list

# Sample input: moveThings(['a', 'b', 'c', 'd', 'e', 'f'], 2, 4)
# Sample Output:           [‘a’, ‘b’, ‘d’, ‘e’, ‘c’, ‘f’]
