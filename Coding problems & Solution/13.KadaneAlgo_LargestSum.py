nums =   [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

import sys
def LargestSum(nums):
  if len(nums)>1:
    LargestSum=0
    maxLargeSum= -sys.maxsize-1 # maximum sum
    for i in range(0,len(nums)):
        LargestSum=LargestSum+nums[i]
        if LargestSum < nums[i]:
           LargestSum=nums[i]
        if maxLargeSum<LargestSum:
           maxLargeSum=LargestSum
    return maxLargeSum
  else:
    return sum(nums)

LargestSum(nums)

