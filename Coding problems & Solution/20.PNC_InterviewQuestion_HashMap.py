# Task description
# Mary has N candies. The i-th candy is of a type represented by an integer
# `
# candies[i]`
# .
# Mary's parents told her to share the candies with her brother. She must give him exactly half the candies. Fortunately, the number of candies N is
# even.
# After giving away half the candies, Mary will eat the remaining ones. She likes variety, so she wants to have candies of various types. Can you find
# the maximum number of different types of candy that Mary can eat?
# Write a function:
# def solution(candies)
# that, given an list `
# candies
# `
# of N integers, representing all the types of candies, returns the maximum possible number of different types of candy
# that Mary can eat after she has given N/2 candies to her brother.
# For example, given:
# candies = [3, 4, 7, 7, 6, 6]
# the function should return 3. One optimal strategy for Mary is to give away one candy of type 4, one of type 7 and one of type 6. The remaining
# candies would be [3, 7, 6]: three candies of different types.
# Given:
# candies = [80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]
# the function should also return 3. Here, Mary starts with ten candies. She can give away five candies of type 80 and the remaining candies would be
# [1000000000, 123456789, 80, 80, 80]. There are only three different types in total, i.e. 80, 1000000000 and 123456789.
# Write an efficient algorithm for the following assumptions:
# - N is an integer within the range [2..100,000];
# - N is even;
# - each element of list `
# candies
# ` is an integer within the range [1..1,000,000,000




def solution(candies): 
    # candies = [3, 4, 7, 7, 6, 6]    I forgot to comment this line and thats the problem 
    GivenCandiesCount = len(candies) / 2

    CandiesCounter = {}
    for i in candies:
        if i not in CandiesCounter:
            CandiesCounter[i] = 1
        else:
            CandiesCounter[i] += 1

    print(GivenCandiesCount)
    print(CandiesCounter)

    CandiesCounter = dict(sorted(CandiesCounter.items(), key=lambda x: x[1]))
    for j, val in CandiesCounter.items():
        if GivenCandiesCount > 0:
            if CandiesCounter[j] == 1:
                GivenCandiesCount = (GivenCandiesCount - CandiesCounter[i])
                CandiesCounter[j] = 0
            elif CandiesCounter[j] < GivenCandiesCount:
                GivenCandiesCount = (GivenCandiesCount - CandiesCounter[i]) + 1
                CandiesCounter[j] = 1
            else:
                CandiesCounter[j] = CandiesCounter[i] - GivenCandiesCount
                GivenCandiesCount = 0

    leftcandiescount = 0
    for i, val in CandiesCounter.items():
        if val > 0:
            leftcandiescount += 1

    return leftcandiescount

if __name__ == '__main__':
    print(solution([3, 4, 7, 7, 6, 6]))


# Alternate solution Preparted in Plane 

CandiesConter ={}
candies = [80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]
giveaway=len(candies)//2
giveaway

for onecandy in candies:
    if onecandy not in CandiesConter:
        CandiesConter[onecandy]=1
    else:
        CandiesConter[onecandy]+=1
CandiesCounter_List= sorted(CandiesConter.items(),reverse=True,key=lambda x:x[1])
print(CandiesCounter_List)

for Item in range(len(CandiesCounter_List)):
   DictVal=CandiesConter[CandiesCounter_List[Item][0]]
   print(f"PRE {Item} {len(CandiesCounter_List)=} {CandiesCounter_List[Item]=} {giveaway=} {DictVal=}")
   
   if giveaway==0:
      break 
   elif DictVal >giveaway :
      giveaway = 0
      CandiesConter[CandiesCounter_List[Item][0]]=DictVal-giveaway 
   elif DictVal <giveaway:
      giveaway=giveaway-(DictVal-1) 
      CandiesConter[CandiesCounter_List[Item][0]]=1

   elif DictVal ==giveaway and Item==len(CandiesCounter_List)-1:
      giveaway=0
      CandiesConter[CandiesCounter_List[Item][0]]=0
   elif DictVal ==giveaway:
      giveaway=1
      CandiesConter[CandiesCounter_List[Item][0]]=1

   print(f"POST {Item} {CandiesCounter_List[Item]=} {giveaway=} {DictVal=}")

result=[]
for i in CandiesConter.keys():
   if CandiesConter[i]>0:
      result.append(i)
print('Final= ',result)