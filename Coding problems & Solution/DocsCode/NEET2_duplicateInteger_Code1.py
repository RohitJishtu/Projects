

# 11. Container With Most Water
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
# PsedoCode 


# Return_Max_water=0
# left,X1=height[0] , 1
# right,X2=height[len(height] ,len(height)+1
# Max_Water=0
# If left< right:
# 	Max_water= left*(X2-X1)  1*9= 9 
# 	Left++
# 	X1++ =2
# Elif right >left:
# 	Max_water=right*(X2-X1)  49
# 	Right –
# 	X2 – =7
# Elif right=left:
# 	Max_water=right*(X2-X1)  40
# If Return_Max_water  > Max_water:
# 	Then swap 
# 	Return_Max_water=49



class Solution:
    def maxArea(self, height: list[int]) -> int:
        return_max_water = 0
        left = 0
        X1 = 1
        right = len(height) - 1
        X2 = len(height)
        
        for element in height:
            current_max_water = 0
            if height[left] <= height[right]:
                current_max_water = height[left] * (X2 - X1)
                left += 1
                X1 += 1
            elif height[left] > height[right]:
                current_max_water = height[right] * (X2 - X1)
                right -= 1
                X2 -= 1
                # return return_max_water
            print(f'{height[left]=},{height[right]=} {X1=} {X2=},{current_max_water=}')
            return_max_water = max(return_max_water, current_max_water)
        
        return return_max_water

# Step 1: Create an instance of the Solution class
solution = Solution()

# Step 2: Define the input list (height values)
height = [1,3,2,5,25,24,5]

# Step 3: Call the maxArea method and print the result
result = solution.maxArea(height)
print("Maximum Water:", result)