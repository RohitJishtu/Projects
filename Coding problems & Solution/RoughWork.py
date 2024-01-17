#============================================================================================
# PYTHON -- 5 Questions 60 mins --Opttimised Approach Required 
#============================================================================================


2. Longest Common Subsequence: https://lnkd.in/gn_niUMG




3. Permutations: https://lnkd.in/gkfWBuk8


# 46. Permutations
# Medium
# Topics
# Companies
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]


# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]


# Recusrion Problem 

# 1 : Run this loop twice 

# recusrion 
#   Check if its tin result 
#   1 2 3..add to ouput 
#   remove them leave only 1 , 
#   once no other choices are there , move to next element 



nums = [1,2,3]
def MainFunction(nums):
    output=[]
    def CreatePermutation(nums,index,output):
      tempoutput =[]
      availablelist= [x for x in nums if x != index]
      tempoutput.append(index)
      for i in range(len(availablelist)):
          tempoutput.append(availablelist[i])
          print('tempoutput ',tempoutput)
          print('output ',tempoutput)
          if  len(tempoutput) == len(nums):
              if tempoutput not in output:
                output.append(tempoutput)
                CreatePermutation(sorted(availablelist,reverse=True),index,output)
              else:
                print('Am I here')
                tempoutput.pop(1)
      print('returning output is ',output)
      return output


    for i in nums:
       output.append(CreatePermutation(nums,i,output))
    return output




5. Merge Intervals: https://lnkd.in/gbFQ-BX9

#============================================================================================
# SQL 
#============================================================================================
