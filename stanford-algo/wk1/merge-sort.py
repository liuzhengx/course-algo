
# New version

def split_list(my_list:list):
  length = len(my_list)

  list_left = my_list[:length//2]
  list_right = my_list[length//2:]

  return list_left, list_right

def merge_list(list1:list, list2:list):
  length = int(len(list1) + len(list2))

  j = 0
  k = 0

  list_merged = []

  for i in range(length):
    if j == len(list1):
      list_merged += list2[k:]
      break
    elif k == len(list2):
      list_merged += list1[j:]
      break

    if list1[j] < list2[k]:
      list_merged.append(list1[j])
      j += 1
    else:
      list_merged.append(list2[k])
      k += 1
      
  return list_merged

def merge_sort(my_list:list):
  length = len(my_list)
  list_left, list_right = split_list(my_list)
  list_merged = []
  
  if length == 0 or length == 1:
    list_merged += merge_list(list_left, list_right)
    return list_merged
  else:
    merged_left = merge_sort(list_left)
    merged_right = merge_sort(list_right)

    list_merged = merge_list(merged_left, merged_right)
    return list_merged

from numpy import random
a = list(random.randint(0,20, 10))
print(a)
print(merge_sort(a))