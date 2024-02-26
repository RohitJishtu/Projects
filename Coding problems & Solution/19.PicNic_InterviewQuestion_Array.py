# Write a function: that, given an array
# `integers
# `
# consisting of N integers, returns the maximum among all one-digit integers. For example, given array
# `integers
# `
# as
# follows:
# [-6,-91, 1011,-100, 84,-22, 0, 1, 473]
# the function should return 1.
# Assume that:
# - N is an integer within the range [1..1,000];
# - each element of array
# `integers
# ` is an integer within the range [−10,000..10,000];
# - there is at least one element in the array which satisfies the condition in the task statement.
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.



def solution(integers):

 # Approach
 # Traverse through the list , if len=1 and its positive then i do teh maximum
  Current_Max=min(integers)
  for i in range(0,len(integers)):
        if len(str(abs(integers[i]))) ==1:
          Current_Max=max(integers[i],Current_Max)
  return Current_Max
 
if __name__ == '__main__':
      print(solution([-6,-91, 1011,-100, 84,-22,-1, 473]))


# Where Did I do the mistake : Only Positive I rerurned 