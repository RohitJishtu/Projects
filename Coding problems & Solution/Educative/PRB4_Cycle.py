# Cuycle Sort 
# If no number is missing True 
# else False 




nums=[3,-3,1,1]
Answer=True

nums=[-2,-1,-3]
Answer=True 

nums=[2,1,-1,-2]
Answer=False 

        



# index=3
# start=0 
# end =0
# newval=num[start]
# while start!=end:
    
#     if +ve move right 
#         end=start+ newval 
#         end =3 
#     else 
#         end = start - newval
#         end = -3 # (from left)
    
#     newval=num[end]
#         if start==end:
#             return True 
    


def FindCycle(nums,index):
    start=index
    end=start
    val=nums[index]
    rotate=0
    print(f'{val=}')
    direction=0
    if val>0:
        start_direction=0
    else:
        start_direction=1
    

    while rotate <len(nums):
        
        if val >0:
            end += val 
            if end>= len(nums):
                end=end%len(nums)
            direction=0
        else:
            end += val 
            if abs(end)>= len(nums):
                end=end%len(nums)
            direction=1
        val=nums[end]
        print(f'{start=} {end=} {val=} {start_direction=}')
        if start==end and start_direction ==direction and rotate>=2 :
            return True 
        elif start==end and start_direction ==direction and rotate<1:
            return 
        
        rotate+=1
    return False 

# nums=[2,1,-1,-2]
# Answer=False 


nums=[3,3,1,-1,2]


# nums=[3,-3,1,1]
# Answer=True

# nums=[-2,-1,-3]
# Answer=True 


for index in range(len(nums)):
    print(FindCycle(nums,index))

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code
