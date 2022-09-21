SS AFK
Anson Wong, Faiza Huda, Kevin Xiao
Codingbat Warmup2
9/21/22
'''
Given a string and a non-negative int n, return a larger string that is n copies of the original string.
'''
def string_times(str, n):
    # can multiply other types (ex: string) not just integers
  return str * n

print("Test cases for string_times")
print(string_times("", 4)) #should return 
print(string_times("xx", 0)) #should return 
print(string_times("Oh gosh ", 2)) #should return Oh gosh Oh gosh
  
'''
Given a string and a non-negative int n,
we'll say that the front of the string is the first 3 chars,
or whatever is there if the string is less than length 3.
Return n copies of the front;
'''
def front_times(str, n):
  return str[0:3] * n

print("Test cases for front_times")
print(front_times('', 4)) #should return 
print(front_times('A', 3)) #should return AAA
print(front_times('afoeha', 2)) #should return afoafo
  
'''
Given a string, return a new string made of
every other char starting with the first,
so "Hello" yields "Hlo".
'''
def string_bits(str):
  new = ''
  i = 0
  while i < (len(str)):
    if i % 2 == 0:
      new += str[i]
    i+= 1
  return new

print("Test cases for string_bits")
print(string_bits('Hello')) #should return Hlo
print(string_bits('')) #should return
print(string_bits('pi')) #should return p
 
'''
Given a non-empty string like "Code"
return a string like "CCoCodCode".
'''
def string_splosion(str):
  new = ''
  for i in range(len(str)+1):
    new += str[0:i]
  return new

print("Test cases for string_splosion")
print(string_splosion('Code')) #should return CCoCodCode
print(string_splosion('ab')) #should return aab
print(string_splosion('x')) #should return x

'''
Given a string, return the count of the number of times
that a substring length 2 appears in the string
and also as the last 2 chars of the string,
so "hixxxhi" yields 1 (we won't count the end substring).
'''
def last2(str):
  new = str[-2:]
  counter = 0
  for i in range(len(str)-2):
    if (str[i:i+2] == new):
      counter +=1
  return counter
print("Test cases for last2")
print(last2('hixxhi')) #should return 1
print(last2('xxaxxaxxaxx')) #should return 3
print(last2('')) #should return 0
print(last2('h')) #should return 0
print(last2('hi')) #should return 0

'''
Given an array of ints,
return the number of 9's in the array.
'''
def array_count9(nums):
  counter = 0
  for i in nums:
    if i == 9:
      counter +=1
  return counter

print("Test cases for array_count9")
print(array_count9([1,2,9])) #should return 1
print(array_count9([9,9,9,9,9,9,9])) #should return 7
print(array_count9([0,23,4])) #should return 0
  
def array_front9(nums):
  if len(nums) < 4:
    for i in nums:
      if i == 9:
        return True
        
    return False
  else:
    for i in range(0,4):
      if nums[i] == 9:
        return True
        
    return False
    
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False
  
