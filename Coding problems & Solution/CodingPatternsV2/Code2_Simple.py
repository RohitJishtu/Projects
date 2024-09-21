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


input=[-6,-91, 1011,-100, 84,-22, 0, 1, 473]
input2=[-6,-91, 1011,-100, 84,-22, 0, 1,2, 473]

# MaxiMum 1 digit inetger 
# Traverse the list 
# keep max 1 digit =0 
#     len(digit) if its 1 then compare with max 
# if new element > max 1 digit , swap 
# else keep


def findMax1DigitInt(input):
    max_1_digit=-9
    for element in input:
        if len(str(element))==1:
            max_1_digit=max(element,max_1_digit)
    return max_1_digit

print(findMax1DigitInt(input))