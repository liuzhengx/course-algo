from numpy import random
from operator import add

# Implement karatsuba algorithim to multiply two integer numbers

# Adding zeroes before the string with smaller length so that two strings have equal lengths
def equal_length(str1: str, str2: str):
  len1 = len(str1)
  len2 = len(str2)
  if len1 != len2:
    len_diff = max(len1, len2) - min(len1, len2)
    if len1 < len2:
      str1 = len_diff * '0' + str1
    else:
      str2 = len_diff * '0' + str2
  else:
    pass
  return str1, str2

# Adding two numbers digit by digit
def add_single(num1:int, num2:int):
  num1 = int(num1)
  num2 = int(num2)
  num1_str, num2_str = equal_length(str(num1), str(num2))
  num1, num2 = [0]*2 + [int(item) for item in list(num1_str)], [0]*2 + [int(item) for item in list(num2_str)]

  # Adding numbers on the corresponding digit
  result = list(map(add, num1, num2))

  # Obtain the numbers to be carried to the next digit, remove the second last-digit, and shift the carriers
  carrier = [1 if item >= 10 else 0 for item in result]
  result = [int(item % 10) if item // 10 == 1 else int(item) for item in result]
  carrier = carrier[1:] + [carrier[0]]
  carrier_store = []

  while carrier != carrier_store and sum(carrier) != 0:
    result = list(map(add, result, carrier))

    # Updating the carrier list
    carrier_store = carrier
    carrier = [1 if item >= 10 else 0 for item in result]

    result = [int(item % 10) if item // 10 == 1 else int(item) for item in result]
    carrier = carrier[1:] + [carrier[0]]

  return int(''.join(str(num) for num in result))

# Splitting a string into halves
def num_split(num:str):
  num_a = num[:len(num)//2]
  num_b = num[len(num)//2:]
  return int(num_a), int(num_b)

# Recursive integer multiplication
def mult_recur(num1: int, num2: int):
  error_list = []
  num1_str = str(num1)
  num2_str = str(num2)
  len1 = len(num1_str)
  len2 = len(num2_str)
  length = int(max(len1, len2))

  if length % 2 == 1:
    length += 1

  num1_str, num2_str = equal_length(num1_str, num2_str)

  if len1 == 1:
    return num1 * num2
  else:
    a, b = num_split(num1_str)
    c, d = num_split(num2_str)

    ac = mult_recur(a, c)
    bd = mult_recur(b, d)
    bc = mult_recur(b, c)
    ad = mult_recur(a, d)

    term1 = int(10**length * ac)
    # Error happened here, length/2 was not an integer due to the floating number, so had to either impose the integer type
    # or using // the floor division
    term2 = int(10**int(length/2) * (ad + bc))
    term3 = int(bd)
    result = add_single(add_single(term1, term2), term3)
    if result != int(num1_str) * int(num2_str):
      error_list.append({'data': (int(num1_str), int(num2_str)), 'ac': ac, 'ad': ad, 'bc': bc, 'bd': bd})
      print('------------The ABOVE------------')

    return add_single(add_single(term1, term2), term3)
    
# The following was a previous attempt to develop the grade school multiplication algorithm
# ----------------------------------------------
# def mult_single(num1:str, num2:str):
#   result = ''
#   to_add = 0
#   for item1 in num1[::-1]:
#     for item2 in num2[::-1]:
#       mult = int(item1) * int(item2) + to_add
#       mult = str(mult)[::-1]
#       if len(mult) == 2:
#         to_add = int(mult[1])
#       else:
#         to_add = 0
#       result += str(mult)[0]
#   result += str(to_add)
#   return int(result[::-1])

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print(mult_recur(x,y))