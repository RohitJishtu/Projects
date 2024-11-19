# Find Minimum Number of Meeting Rooms
# Given a list of meeting time intervals, find the minimum number of conference rooms required.
# Example:
# Input: [[0, 30], [5, 10], [15, 20]]
# Output: 2


# Input: [[0, 30], [ 1 - 30  , 2- 35  ,3-  ]
#         [5, 10], 2   
#         [15, 20]] 2 


# process : Provided they are ascending 

Input= [[0, 30], [5, 10], [35, 40]]
def FindMinRooms(Input):
    room_map={}
    room_no=1
    room_map[room_no]=Input[0][1]
    for meeting in Input[1:]:
        start=meeting[0]
        end=meeting[1]
        if start < room_map[room_no]:
            room_no+=1
            room_map[room_no]=end
        else:
            room_map[room_no]=end
    
    return len(room_map)

print(FindMinRooms(Input))



Ques =  {
          Please Rate my above written [Code].
          Give me rating out of 5 with respect to interviews. 
          Give Time complexity 
          Give Space complexity 
          Also list down Coder's stregths and weaknesses 
          Add Comments for the code , dont change anything in the code 
        }
