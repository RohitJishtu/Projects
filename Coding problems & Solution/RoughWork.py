2. Longest Common Subsequence: https://lnkd.in/gn_niUMG
3. Permutations: https://lnkd.in/gkfWBuk8
5. Merge Intervals: https://lnkd.in/gbFQ-BX9

===============19 Jan ==============================

#1. ###------------------------------------------------------
#Only a element should be printed once in a string 
# My best program
#IPString = ("swasti ksingh")

# Can use set 

#2. ###------------------------------------------------------
Common between 2 strings 
array1=['a','b','c','d','e']
array2=['z','f','p','d','r','s']


#3. ###------------------------------------------------------
Anagram 
import string
s = "cbaebabacd"
p = "abc"

#4. ###------------------------------------------------------
--Revenue Milestone 
revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,110,120,130,140,150,160,170,190,200]
milestones = [100, 200, 500,1000,2000]
#output = [4, 6, 10]
output=[]


def WhenWeMetrevenue(revenues,milestones):
    sum=0
    output=[]
    for i in range(0, len(revenues)):
      sum+= revenues[i]
      # print('sum',sum)
      # print('len',len(milestones))
      if sum >= milestones[0] and len(milestones)>0:
          output.append(i+1)
          milestones.pop(0)
          # print('milestone',milestones[0])
    return output


#5. ###------------------------------------------------------

--Kth large emenets 
list = [1,2,33,14,35,11]
n=len(list)


#5. ###------------------------------------------------------

--Combination SUm 
Integers=[2,3,5]
target=8

#5. ###------------------------------------------------------

--Amagram 
import string
s = "cbaebabacd"
p = "abcd"
output=0


#5. ###------------------------------------------------------

--remove duplicates 
nums = [1,1,2]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]


#5. ###------------------------------------------------------

In a given list, find the counts of the minimum value.
List = [5, 2, 8, 1, 5, 0, 3, 1, 7, 2, 5, 4]

# plan , create a minimum value first val  , then iterate 
#       2. insert the counts into dict    
#       1. if val > first val , swap min val 
       

def FindMinval(GivenList):  
  if GivenList: 
    min_val=GivenList[0]
    ManualMap={}
    for i in range(0,len(GivenList)):
      if min_val >= GivenList[i]:
        min_val=GivenList[i]
        if GivenList[i] not in ManualMap:
          ManualMap[GivenList[i]]=1
        else:
          ManualMap[GivenList[i]]+=1
    return ManualMap[min_val]
  else:
    return 'EmptyList'




#5. ###------------------------------------------------------

Q1 Py : Highest Number 
Q2 Py : Highest Frequency Number 
Q3 Py : Merge Interval - maxium Planes in the air QUestion 



#---#---#---#---#---#---#---#---#---#---#---#---#---#---
Calculate the sum of odd numbers in a list.
List = [3, 6, 8, 2, 5, 7, 9, 4, 1]


#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---


Merge Intervals 
Plane Maximum time in Air 
435. Non-overlapping Intervals

