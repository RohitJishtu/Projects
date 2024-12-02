# Problem: Find The Duplicate Number
# Statement
# Given an array of positive numbers, nums, such that the values lie in the range 
# , inclusive, and that there are 
#  numbers in the array, find and return the duplicate number present in nums. There is only one repeated number in nums.





nums2=[1,2,5,4,2,5]
nums3=[1,2,3,4,5,6,6,7]


# LOGIC :

# Iterate through , store the number in dictionary , if found same outoput 
# o(n) time 
# O(n) space 


nums1= [1,3,3,4,2,5]

# step1 : Sort 
# step2 : , use master , runner 
#     master =n , runner checks next , is exists same as master then retur True else , update Master and runner 



def find_duplicate(nums):
    nums=sorted(nums)
    master =0
    runner=0
    for i in range(len(nums)-1):
        master=nums[i]
        runner=nums[i+1]
        if master==runner:
            return master 


# print(find_duplicate(nums3))

assert find_duplicate(nums1)==3
assert find_duplicate(nums2)==2
assert find_duplicate(nums3)==6

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code
