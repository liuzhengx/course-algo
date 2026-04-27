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
  
# The above codes are copied from merge-sort.py


# Counting the inversion using merge sort
def cross_count(list1:list, list2:list):
  length = int(len(list1) + len(list2))

  j = 0
  k = 0
  count_inversion = 0

  for i in range(length):
    if j == len(list1):
      break
    elif k == len(list2):
      break

    if list1[j] < list2[k]:
      j += 1
    else:
      k += 1
      count_inversion += (len(list1) - j)
  return count_inversion


def count_inversion(my_list:list):
  length = len(my_list)

  if length <= 1:
    return 0
  else:
    left_list, right_list = my_list[:length//2], my_list[length//2:]

    left_inversion = count_inversion(left_list)
    right_inversion = count_inversion(right_list)
    cross_inversion = cross_count(merge_sort(left_list),merge_sort(right_list))
    total_inversion = left_inversion + right_inversion + cross_inversion
  return total_inversion

import pandas as pd

raw_data = pd.read_csv('/Users/liuzhengxun/Documents/GitHub/course-algo/stanford-algo/wk2/IntegerArray.txt', header = None)

data = list(raw_data[0])

print(count_inversion(data))
