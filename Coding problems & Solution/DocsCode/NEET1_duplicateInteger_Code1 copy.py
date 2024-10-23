# Duplicate Integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false
nums = [1, 2, 3, 2]
def duplicatElements(nums):
    if len(nums)>1:
        element_map={}
        for element in nums:
            if element in element_map:
                return True 
            else:
                element_map[element]=1
    return False 

print(duplicatElements(nums))


Time Complexity : O(n)
Space =O(n)


# # LLm Evaluation 

# Ques = 
#         [
#           Please Rate my above written [Code].
#           Give me rating out of 5 with respect to interviews. 
#           Give Time complexity 
#           Give Space complexity 
#           Also list down Coder's stregths and weaknesses 
#           Add Comments for the code , dont change anything in the code 
#         ]

