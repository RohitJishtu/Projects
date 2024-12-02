
# 3 Find the lement in rotated Array 

# Input  : arr[] = {4, 5, 6, 7, 0, 1, 2}, key = 0
# Output : 4


# Input  : arr[] = { 4, 5, 6, 7, 0, 1, 2 }, key = 3
# Output : -1


# Input : arr[] = {50, 10, 20, 30, 40}, key = 10   
# Output : 1


array = [50, 10, 20, 30, 40]
output=1

def FindElement(array,key=0):

    left=0 
    right=len(array)-1
    mid=0	
    while left <= right:
        mid= (left+right)//2  
        print(f'{array[mid]=} {array[left]=} {array[right]=}')
        if array[mid]==key:
            return mid 
		
        elif array[left]<= array[mid] :    
            if array[left]<key<array[mid]:
                right=mid-1
            else:
                left=mid+1
        else:
            if array[mid]<key<array[right]:
                left=mid+1
            else:
                right=mid-1
    return -1 

print(FindElement(array,key=10))

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code
