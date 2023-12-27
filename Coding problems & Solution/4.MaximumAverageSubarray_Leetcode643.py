# 643. Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has
# the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000


# 1,12,-5,-6 /4  Avg= 10
# 2-6 Avg , if Avg > PreAvg , replace else


nums = [9, 7, 3, 5, 6, 2, 0, 8, 1, 9]
k = 6
i = 0
avgStr = -99999
limit = len(nums) % k
print('limit', limit)
print('nums length', len(nums))
runningsum = sum(nums[:k])
runningavg = runningsum / k
print('runningAvg', runningavg)
i = 1

# Check for special cases where the length of nums is 1 or equal to k
if len(nums) == 1 or len(nums) == k:
    print('RESULT', i, runningavg)
else:
    # Iterate through the array using a sliding window approach
    while i <= (len(nums) - (k)):
        # Update the running sum for the current window
        runningsum = runningsum - nums[i - 1] + nums[i + (k - 1)]
        # Calculate the average for the current window
        Avg = runningsum / k
        print('i and result outside', i, runningsum, Avg)
        
        # Update the maximum average if the current average is greater
        if Avg > runningavg:
            runningavg = Avg
            print('RESULT', i, runningavg)
        
        i = i + 1

