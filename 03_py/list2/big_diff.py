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
    
