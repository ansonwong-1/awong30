'''
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
'''

def count_evens(nums):
  x = 0
  y = 0
  while x < len(nums):
    if nums[x] % 2 == 0:
      y += 1
    x += 1
  return y
print(count_evens([2, 1, 2, 3, 4])) #should return	3

      
'''

Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
'''
      
def big_diff(nums):
  x = 1
  bignumber = nums[0]
  smallnumber = nums[0]
  while x < len(nums):
    if nums[x] > bignumber:
      bignumber = nums[x]
    if nums[x] < smallnumber:
      smallnumber = nums[x]
    x += 1
  return bignumber - smallnumber
print(big_diff([10, 3, 5, 6])) # should return 7

      
      
'''

Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
'''
def centered_average(nums):
  x = 1
  bignumber = nums[0]
  smallnumber = nums[0]
  y = nums[0]
  while x < len(nums):
    if nums[x] > bignumber:
      bignumber = nums[x]
    if nums[x] < smallnumber:
      smallnumber = nums[x]
    y += nums[x]
    x += 1
  y = y - bignumber - smallnumber
  y = y / (len(nums)-2)

  return y
print(centered_average([1, 2, 3, 4, 100])) # should return 3
  
    
'''

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

'''
      
def sum13(nums):
  x = 0
  sum = 0
  while x < len(nums):
    if nums[x] != 13:
      sum += nums[x]
    else:
      x = x + 1
    x += 1
  return sum
      
print(sum13([1, 2, 2, 1])) #should return 6
    
'''
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
'''
def sum67(nums):
  x = 0
  sum = 0
  y = 1
  z = 0
  counter = False
  while x < len(nums):
    if nums[x] == 6 and counter == False:
      y = x
      counter = True
    if nums[x] == 7 and counter == True:
      z = x
      counter = False
    while y <= z:
      sum -= nums[y]
      y += 1
    sum += nums[x]
    x += 1
  return sum
print(sum67([1, 2, 2])) # should return 5
      
'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
'''
def has22(nums):
  x = 1
  pog = False
  while x < len(nums):
    if nums[x-1] == 2 and nums[x] == 2:
      pog = True
    x += 1
  return pog
print(has22([1, 2, 2])) # should return True



  
