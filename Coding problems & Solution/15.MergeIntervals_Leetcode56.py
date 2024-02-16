
# 56. Merge Intervals
# Medium
# Topics
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.




# Approach 

# Step1 : Sort the 2d array based on first val
# Step2 : low = a[0][0] 
#         high= a[0][1]

# step 3 :
#         for i in len(array)--starts from second element 
#         if 
#           first val of second is less than high 
#           update high = to secnd val 
#           pop array 
#           make new entry in array with existing low and new high 
#         else 
#           add entry with new low and new high 

# step 4 : close 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals=sorted(intervals,key=lambda x:x[0],reverse=False)

        low= intervals[0][0]
        high=intervals[0][1]

        output=[]
        output.append((low,high))

        for i,j in intervals:
            if  i  <= high and j>=high:
                 high=j
                 output.pop()
                 output.append((low,high))
            elif j <= high:
                 continue
            else:
                 high=j
                 low=i
                 output.append((low,high))

        return output
