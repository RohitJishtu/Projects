# Cuycle Sort 
# If no number is missing True 
# else False 


# nums=[1,4,5,2,9]
# MissingNumber=2


# Logic 

# I start from first element 


# if O < element < len(list):
#     swap , element and Sequence 
#     if array[seqnec] not found then thats the element 

# else:
#     This Number is out of range , we can ignore it and move ion 


nums=[1,4,5,2,9]

def MissingNo(nums):
    Seq=0
    CorrectPlace =1

    while Seq<=len(nums):
            CorrectPlace=nums[Seq]
            CorrectPlace-=1
            if nums[CorrectPlace]!=nums[Seq] and nums[Seq]<=len(nums):
                nums[CorrectPlace],nums[Seq]=nums[Seq],nums[CorrectPlace]
                print('swapped')
            else:
                Seq+=1
            print(f'{CorrectPlace=} {nums[CorrectPlace]=} {Seq=} {nums=}')


print(MissingNo(nums))

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code
