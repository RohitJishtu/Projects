# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.


nums=[10,5,2,6]
k=100
output= [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]


# Approach - recursive 

# Step 1 :  if i < target insert into output 
#           pool.ppend(i)
#           product=newproduct  
#           append(pool)  
#           else we do not append 
 
# step 2 :  newproduct=product*5  [same step 1 ]

def FinDproducts(nums,k):
    output=[]
    latestprod=1
    def BackTrack(nums,latestprod,k,temparray=[]):

        print(f'{output=} {nums=}')
        if len(nums) == 0:
            temparray=[]
            return 
        
        if latestprod < k and len(temparray)>0:
           output.append(temparray)

        elif latestprod > k and len(temparray)>0:
            temparray=[]
            return  
            
        nums2=nums.copy()
        for element in range(len(nums)):
            if nums[element] < k:
               temparray.append(nums[element])
               newlist=[]
               newlist.append(nums[element])
               output.append(newlist)
               latestprod=latestprod*element
               nums2.pop(0)
               BackTrack(nums2,latestprod,k,temparray)
            else:
               nums2.pop(0)
               
               BackTrack(nums2,latestprod,k,temparray) 

    BackTrack(nums,latestprod,k)
    return output


FinDproducts(nums,k)