# I have an array as input 
Nums=[2,3,5]
Target=8

# we have to find combination where the array matches the target 
# Process 

# Step1 : Start from 2 , index =0 , keep adding itself until 

#                 1. Sum <Target : keep adding itself to array 
#                 2. Sum > Target : remove latest element and increase index to next 
#                 3. Sum==Target : Append temparray to main output and remove latest added and move to next 

# Step2 : Go to next element and Repeat the process  

def CombinationSum(Nums,Target):
    Output=[]
    def Backtrack(Nums,index,Target,Output,TempA=[],Sum=0):    # 2, index=0
        print(f'called from {Nums=}  {index=} {Target=} {Output=} {TempA=} {Sum=}')
        for  element in range(index,len(Nums)):
                Sum+=Nums[element]
                TempA.append(Nums[element])    
                if Sum==Target:
                    Output.append(TempA)
                    print(f'Inside Equal {Nums=}  {index=} {Target=} {Output=} {TempA=} {Sum=}')
                    Sum-=Nums[element]
                    TempA.pop()
                    return 
                   
                elif Sum < Target:
                    #TempA=[2,2,2,2] , [2,2,2,5] 
                    Backtrack(Nums,index,Target,Output,TempA,Sum)
                    
                else:
                    Sum-=Nums[element]
                    TempA.pop()
                    Backtrack(Nums,index+1,Target,Output,TempA,Sum)
            
    Backtrack(Nums,0,Target,Output)

CombinationSum(Nums,Target)