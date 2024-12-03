
# Question : we ll have to make sure the priority task gets done first 


# InputData , insert into a list [[Task1,1], [Task2,2], [Task3 ,1]]
# Min Heap- 

# See All Tasks 
#   print heap   

# Execution of Top Priority task 

# 0(n), o(1), o(n)

InputData = ('Task',2)
InputData2 = ('Task2',2)
InputData3 = ('Task3',1)
InputData3 = ('Task8',0)

import heapq
def InsertHeap(InputData,heap):
    heapq.heappush(heap,(InputData[1],InputData[0]))
    return heap 

def Printtaks(heap):
    print('original heap',heap)
    newlist=[]
    for element in heap:
        topelement= heapq.heappop(heap)
        newlist.append(topelement)
    print(newlist)


def __main__():
    print('Start')
    # Insert into healp 
    heap=[]
    InsertHeap(InputData,heap)
    InsertHeap(InputData2,heap)
    InsertHeap(InputData3,heap)

    # Sell All tasks 
    Printtaks(heap)

    # # Sell All tasks 
    # what is the top priority tasks 

    # print(heapq.heappop(heap))



if __name__ == "__main__":  # Ensure the function is called when the script is run directly
    __main__()

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code
