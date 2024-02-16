
# 435. Non-overlapping Intervals
# Medium
# Topics
# Companies
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


# Approach : 1.sort based on first elemnt 
# 2. next = i,j if high > i then count =1 , 
#     if high > j then high else high=j
# 3.

# intervals=[[1,100],[11,22],[1,11],[2,12]]=2

# intervals= [[1,2],[2,3],[3,4],[1,3]] =1
# [[1,2],[2,3]]

# intervals=[[1,2],[1,2],[1,2]]=2
# intervals=[[0,2],[1,3],[2,4],[3,5],[4,6]]=2


intervals=[[1,2],[2,3],[3,4],[1,3]]


# intervals=[[1,2],[2,3]]

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        interval=sorted(intervals)
        OverlapCounter=0
        low=intervals[0][0]
        high=intervals[0][1]

        for i, j in interval:
            if i < high:
              OverlapCounter+=1
              if j < high:
                high=j
            else:
                high=j
           
        return OverlapCounter-1

Obj1=Solution()
Obj1.eraseOverlapIntervals(intervals)
