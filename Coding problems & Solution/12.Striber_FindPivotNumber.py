nums=[1,7,3,6,5,None]

nums=[x for x in nums if x is not None]

def FIndPivotString(nums):
  if nums:
    rsum=sum(nums)
    lsum=0
    for i in range(0,len(nums)):
        if i >0:
          lsum=lsum+nums[i-1]
        rsum=rsum-nums[i]
        if lsum==rsum:
          return i 
  return -1 
FIndPivotString(nums)