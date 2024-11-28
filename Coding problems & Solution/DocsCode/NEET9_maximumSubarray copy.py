# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

nums = [1,12,-5,-6,50,3]
k = 4

def MaxSubArray(nums,k):    
    max_average=0
    sum=0
    seq=1
    for element in nums:
        print(f'{element=} {max_average=} {sum=} {seq=}')
        sum+= element
        if sum > element:
            seq+=1
        else:
            seq=1
            sum=element 
        if seq==k:
            max_average=max(max_average,sum/seq)
    return max_average

print(MaxSubArray(nums,k))

# Based on the code provided above, please answer the following questions:

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code

