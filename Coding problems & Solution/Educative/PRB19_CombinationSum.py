# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

# Logic :

# Traverse through array 
# 10 if num is big than target , return 
# 1 :  start collecting this in temparray 
    # with every collection append to array if sum<target with next index 
    # if its =target return 
    # if its greater return 

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

def CandidatesTarget(candidates,target):
    Output=[]
    sum=0

    def recur(candidates,index,sum,Output,temp=[]):
            if sum==target:
               Output.append(temp[:])
               return 

            if sum > target:
                return 
            
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                temp.append(candidates[i])
                sum+=candidates[i]
                recur(candidates,i+1,sum,Output,temp)
                temp.pop()
                sum-=candidates[i]
            return Output

    return recur(candidates,0,0,[])
candidates = [10,1,2,7,6,1,5]
target = 8

print(CandidatesTarget(candidates,target))


# def CandidatesTarget(candidates, target):
#     def recur(candidates, index, current_sum, temp, result):
#         # Base case: if the sum equals the target, add the combination
#         if current_sum == target:
#             result.append(temp[:])  # Add a copy of the current combination
#             return
        
#         # If the current sum exceeds the target, terminate this path
#         if current_sum > target:
#             return

#         # Iterate through the candidates starting from the current index
#         for i in range(index, len(candidates)):
#             # Skip duplicates
#             # if i > index and candidates[i] == candidates[i - 1]:
#             #     continue

#             # Include the current number and recurse
#             temp.append(candidates[i])
#             current_sum+=candidates[i]
#             recur(candidates, i + 1, current_sum, temp, result)
#             # Backtrack by removing the last added number
#             temp.pop()
#             current_sum-=candidates[i]

#     # Sort candidates to handle duplicates and enable early stopping
#     candidates.sort()
#     result = []
#     recur(candidates, 0, 0, [], result)
#     return result

# # Example 1
# candidates1 = [10, 1, 2, 7, 6, 1, 5]
# target1 = 8
# print(CandidatesTarget(candidates1, target1))

# # Example 2
# candidates2 = [2, 5, 2, 1, 2]
# target2 = 5
# print(CandidatesTarget(candidates2, target2))
