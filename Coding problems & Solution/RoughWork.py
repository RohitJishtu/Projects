#============================================================================================
# PYTHON -- 5 Questions 60 mins --Opttimised Approach Required 
#============================================================================================


2. Longest Common Subsequence: https://lnkd.in/gn_niUMG
3. Permutations: https://lnkd.in/gkfWBuk8
5. Merge Intervals: https://lnkd.in/gbFQ-BX9

===============19 Jan ==============================

----------------


In a given list, find the counts of the minimum value.

List = [5, 2, 8, 1, 5, 0, 3, 1, 7, 2, 5, 4]


#--------------------------------#----------------#

Given a list, remove duplicate elements and return the modified list.

List = [10, 20, 30, 10, 40, 50, 20, 60]

#--------------------------------#----------------#

Calculate the sum of odd numbers in a list.

List = [3, 6, 8, 2, 5, 7, 9, 4, 1]

#--------------------------------#----------------#

Merge two lists into a single list and sort them in descending order.

List1 = [15, 8, 12, 10]

List2 = [7, 20, 18, 25]

#--------------------------------#----------------#

Find the product of all the elements in a given list.

List = [2, 3, 5, 7, 10]


#--------------------------------#----------------#

Count characters in a string and create a dictionary with character counts.

my_string = "hellothere"


#--------------------------------#----------------#

Concatenate the strings from the list based on the number of occurrences of the dictionary keys, and return the resulting string.

my_list = ["apple", "orange", "banana", "grape"]
my_dict = {"a": 0, "o": 2, "e": 1}


#--------------------------------#----------------#

Sort a list of strings based on the length of each string, and store the result in a dictionary.

word_list = ["python", "java", "c", "javascript", "ruby"]

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
