

NewList=[]

# Find Duplicates 
# Dictionary : When you find something which is already there in dictionary , then you print that out 

def FindDuplicates(NewList):
    map={}
    if NewList and len(NewList)>0:
        for element in NewList:
            if element in map:
                return element 
            else:
                map[element]=1
    else:
        return 'Empty Array'
    return 'No Duplicates'

print(FindDuplicates(NewList))


# Prompt:

# Based on the code provided above, please answer the following questions:

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
