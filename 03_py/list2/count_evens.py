def count_evens(nums):
  x = 0
  y = 0
  while x < len(nums):
    if nums[x] % 2 == 0:
      y += 1
    x += 1
  return y
