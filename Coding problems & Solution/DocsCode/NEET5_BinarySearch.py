
# Binary Search and Variants 
# 	array=[1,6,7,9,10,12]
# 	SerachElement = 8 	
# Result , position or None if not in the list 
# Q: part 1 of QUestion 

# array=[1,6,7,9,10,12]
# element=1
# def SerachElement(array, element):
#     left = 0
#     right = len(array)
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == element:
#             return mid
#         elif array[mid] < element:
#             left = mid + 1
#         elif array[mid] > element:
#             right = mid - 1
#     return None

#------------------------------------------------------------------------------------------------------------

# Q: part 2 of QUestion  : what if we have a twisted sorted array.
# array=[9,10,12,1,6,7]
# element=9


# 13 > 9 and 
# if mid < element and array[right] < element :
# 	 take to left part 
# elif mid > element and array[right] >= element 
# 	take to right part 
# 	mid < element 
# print(SerachElement(array, element))


array = [12, 1, 6, 7, 9, 10]
element=7
def SearchElement_twistedArray(array, element):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right) // 2
        print(f'{left=}, {right=} ,{mid=}')
        if element == array[mid]:
            return mid
        elif  array[mid] < element < array[right]:
            print('right side 1')
            left=mid+1
			mid=left+right//2
			if  array[left] < element < array[mid]:
            
			else:
                 

        elif array[mid] > element > array[left]:
            print('left side 1')
            right = mid - 1
            
    return None

print(SearchElement_twistedArray(array, element))