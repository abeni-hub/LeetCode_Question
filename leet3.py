def two_sum(nums, target):
  num_dict = {}

# Iterate through the array
for i,num in enumerate(nums):
  current = target - num
  if current in num_dict:
    return [num_dict[complement], i]

  num_dict[num] = i
