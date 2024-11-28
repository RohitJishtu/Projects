# Problem: Sum of Three Values
# Statement
# Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such integers exist in the array. Otherwise, return FALSE.


nums= [3,7,1,2,8,4]
target = 20
result = True 

# Target=1
# nums= [-1,2,1,4]
# result=False 

# target =1 
# nums=  [-1,2,1,4,-2]
# result=True 


# nums= [3,7,1,2,8,4,5]
# target = 20
# result = True 



# nums
# target-num = num2 
# if num2:
#     target-num1-num2=num3 
# if num3 exists , we are done 

# LOGIC 

# Step1 : iterate 
# Step2 : first element - subtract target by that element and make new target 

#         step 3 : Rest of the array treat as 2 sum , every element insert in dictionary the target-element and 
#         step 4 : if new element is already there we get our threesum 
# step 5: we go back to element 1 and move to element 2 



nums= [3,7,1,2,8,4,5]
target = 20
def ThreeSUmFlag(nums,index,target):
    target-=nums[index]
    map={}
    for element in nums[index+1:]:
        # print(f'{target-element=} {map=} ')
        if target-element not in map:
            map[element]=1
        else:
            return True 
       
for index in range(len(nums)):
    if ThreeSUmFlag(nums,index,target)==True:
       print('True')
       break 
    elif index==len(nums)-1:
       print('False')


# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code
