
# 3 Find the lement in rotated Array 




# Logic 

# if len(Arr)==1

# pivot = mid of array 
# if elements are less than pivot - i put them in left array 
# if greater I put them in right 

# return left+ middle +right 

Array=[1,5,3,7,6,4]
def quickSort(Array):

    print(f'starting iterating with {Array=}')
    if len(Array)<=1:
        print('returning this array ',Array)
        return  Array

    left_val=0
    right_val =len(Array)
    pivot = (left_val+right_val)//2

    left=[]
    right=[]
    for element in Array:

        if element>Array[pivot]:
            right.append(element)
        elif element<Array[pivot]:
            left.append(element)
    

    pivotlist=[]
    pivotlist.append(Array[pivot])
    return quickSort(left) +pivotlist + quickSort(right)


Array=[1,5,3,7,6,4]
print(quickSort(Array))