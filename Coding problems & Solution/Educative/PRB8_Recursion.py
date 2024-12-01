# Combination SUm Kind of problem 



# Logic 

# start from 2 , keep adding 2 until it exceeds target 

# backtrack(array,index,temp,sum) 
# loop array from index to last element 
#         sum+= nextelement 
#         temp.append(nextelement)
#     1. if sum==target:
# #         return temp
#           add to main , and remove latest , go to next element in the array 

#     2. if sum > target 
            # remove laste added number , decrease sum 

    # 3. if sum <target 
    #        # keep on adding number 
                                    
                                                       

def Combination_Sum(Array,target):
    index=0
    output=[]
    def backtrack(Array,index,temp=[],sum=0):
        print(f'{Array=} {index=} {temp=} {sum=} {output=}')

        if sum==target:
            output.append(temp.copy())
            return 
                
        else:
            return   

        for i in range(index,len(Array)):
            sum+=Array[i]
            temp.append(Array[i])
            print(f'before calling {Array=} {index=} {temp=} {sum=} {output=}')
            backtrack(Array,i,temp,sum)
            sum-=Array[i]
            temp.pop()  
        return output
    return backtrack(Array,index)

Array=[2,3,5]
target=8
# Answer=[[2,2,2,2] , [2,3,3] [3,5]]
print(Combination_Sum(Array,target))

def Combination_Sum(Array, target):
    output = []

    def backtrack(index, temp, current_sum):
        # Base case: if the current sum equals the target
        if current_sum == target:
            output.append(temp.copy())  # Add a copy of the current combination
            return

        # If the current sum exceeds the target, stop exploring
        if current_sum > target:
            return

        # Loop through the array starting from `index` to reuse elements
        for i in range(index, len(Array)):
            temp.append(Array[i])  # Add the current number to the combination
            backtrack(i, temp, current_sum + Array[i])  # Recursive call
            temp.pop()  # Backtrack: remove the last element

    backtrack(0, [], 0)  # Start backtracking from index 0 with an empty combination
    return output


print(Combination_Sum(Array,target))


def Combination_Sum(Array,target):
    index=0
    output=[]
    def backtrack(Array,index,temp=[],sum=0):
        print(f'{Array=} {index=} {temp=} {sum=} {output=}')

        if sum==target:
            output.append(temp.copy())
            return 
                
        else:
            return   

        for i in range(index,len(Array)):
            sum+=Array[i]
            temp.append(Array[i])
            print(f'before calling {Array=} {index=} {temp=} {sum=} {output=}')
            backtrack(Array,i,temp,sum)
            sum-=Array[i]
            temp.pop()  
        return output
    return backtrack(Array,index)

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code
