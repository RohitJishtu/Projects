meetings = [[5, 10], [2, 3]] 
Output= 1
meetings = [[1, 3], [5, 7], [4, 6], [7, 9], [9, 10]]
Output= 2



# ListStart=[1,5,4,7,9] - sort this 
# LisEnd=[3,7,6,9,10]	-sort this 
# i=1, j=1 
# 1 , 2, 3, 4  
# 0   
# i=0,j=0
# For time upto maxtime:
# 	If ListStart[i] = time 
# RoomsUsed = 1  
# i=i+1
# If ListStart[j] = time 
# 	RoomsUsed = 1  
# 	j=j+1


def FindRooms(meetings):
    StartTime=[]
    EndTime=[]
    for start in meetings:
        StartTime.append(start[0])
    
    for end in meetings:
        EndTime.append(end[1])
    
    StartTime=sorted(StartTime)
    EndTime=sorted (EndTime)

    UpperLoopLimit= max(max(StartTime),max(EndTime))
    i=0
    j=0
    roomsused=0
    maxroomused=0
    # print(f'{StartTime=},{EndTime=} {roomsused=} {UpperLoopLimit=}')
    for iter in range(UpperLoopLimit):
            if iter== StartTime[i]:
                 roomsused+=1
                 i+=1
            if iter== EndTime[j]:
                 roomsused-=1
                 j+=1
            # print(f'{iter=} {i=},{j=} {roomsused=}')
            maxroomused=max(maxroomused,roomsused)
    return maxroomused 

meetings = [[1, 3], [5, 7], [4, 6], [7, 9], [9, 10]]
Output= 2

print(FindRooms(meetings))

# Prompt for LLM:

# Based on the code provided above, please answer the following questions:

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code

