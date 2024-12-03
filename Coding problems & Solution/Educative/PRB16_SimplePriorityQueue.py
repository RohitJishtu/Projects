# Input: K = 3, arr = { }
# Output: 0 1 2 3 4 5 6 7 8 9 10 11 


# Input: k = 4, arr = { {1}, {2, 4}, {3, 7, 9, 11}, {13} }
# Output: 1 2 3 4 7 9 11 13

# Logic 

array=[[1, 3, 5, 7], 
[2, 4, 6, 8], 
[0, 9, 10, 11]]
k=3

# 1. first element of each array and push that into a heap 
# 2. take the first element out , and append it to an array 
# 1. repeat the same for the second element of the array where first was taken 





def __main__():
    heap=[]
    
    InsertToHeap(array,k,heap)
    
    while heap:
        for array,element in range(len(array)):
            




    heap=InsertToHeap(array,k)
    print(heap)
    List=[]
    FinalList_Insertion(List,heap)

