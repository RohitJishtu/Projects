# 128. Longest Consecutive Sequence # Medium
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.


# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
# Approach 1

count=1
j=0
maxcount=1
for i in range(0,len(nums)):
   Upside=True  #Positive direction from the number
   Downside=True #negative direction from the number

   while Upside or Downside:
    j+=1
    if Upside:
        if nums[i]+j in nums:
          count+=1
        else:
          Upside=False

    if Downside:
        if nums[i]-j in nums:
          count+=1
        else:
          Downside=False

    if count>maxcount:
        maxcount=count

print(maxcount)