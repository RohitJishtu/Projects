# Input: nums = [2,3,5], k = 8
# Output: [[2,2,2,2] ,[2,3,3] ,[5,3]]





# Approach - recursive 

# Step 1 :   start from ith index 
#             2 : keep adding same until the num exceeeds 

# step 2 :   if it exceeds , remove last number and add next element in the list , repat 1 

#            if numbers are over  

# step 3 :   move to next element and repeat 1 to 3 

nums = [2,3,5]
k = 8
Output= [[2,2,2,2] ,[2,3,3] ,[5,3]]

def CombinationSum(nums,k):
    Output=[]
    start=0
    def backtrack(start,k,sum=0,temp=[]):

        print(f'recursive {sum=} {temp=}')

        for element in range(start,len(nums)):
            temp.append(nums[element])
            sum+=nums[element]
            print(f'{sum=} {temp=}')
            if sum==k:
                Output.append(temp)
                print(f'{Output=} {temp=}')
                temp.pop()
                sum-=element
                return 
            elif sum < k and element < len(nums):
                backtrack(start,k,sum,temp)


            elif element < len(nums):
                temp.pop()
                sum-=nums[element]
                backtrack(start+1,k,sum,temp)
            else:
                temp.pop()
                sum-=nums[element]
                start+=1
                return 

    backtrack(0,k,sum=0,temp=[])
      
    return Output

print(CombinationSum(nums,k))