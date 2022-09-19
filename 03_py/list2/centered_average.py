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
  
    
