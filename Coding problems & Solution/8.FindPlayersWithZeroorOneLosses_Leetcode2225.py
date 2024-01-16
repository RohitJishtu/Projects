# Ques 1


# 2225. Find Players With Zero or One Losses
# Input: 
# matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
# Explanation:
# Players 1, 2, 5, and 6 have not lost any matches.
# Players 3 and 4 each have lost two matches.
# Thus, answer[0] = [1,2,5,6] and answer[1] = [].

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.




matches = [[2,3],
           [1,3],
           [5,4],
           [6,7]
          ]
# Output: [[1,2,5,6],[]]
# output=[[1,2],[3,4]]

output=[None,None]

# Step 1 : result array 
# Step 2:Iterate through the array 
# > Insert in result [0] : Post checking in result 2 
# > Insert in result [1] : if the data is not in result 2 
#         if its there : Then I remove that 


def Insertion(matches):
  output=[[],[]]
  removelist=[]
  for i in range(len(matches)):
        for j in range(2):
          print('i,j',i,j)
          iterator = matches[i][j] 
          if j==0:
            print('len of output',len(output))
            if len(output)>1 and iterator not in output[1]:
              output[0].append(iterator)
            elif iterator not in output[1]:
              output[0].append(iterator)

          else:
            print('output is ',output)
            if iterator in output[1]:
              output[1].remove(iterator)
              removelist.append(iterator)
            elif (iterator not in removelist):
              output[1].append(iterator)
           
  return output     




