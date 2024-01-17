1. Rotate Array: https://lnkd.in/gmNmR_GM



# 189. Rotate Array
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


nums = [1,2,3,4,5,6,7]
k = 11
def RotateArray(nums,k):
  result=nums.copy()
  k=k%len(nums)
  for i in range(len(nums)-k):
      result[i+k]=nums[i]
  for i in range(k):
      result[i]=nums[(len(nums)-k)+i]
  
  return result
  
print(RotateArray(nums,k))