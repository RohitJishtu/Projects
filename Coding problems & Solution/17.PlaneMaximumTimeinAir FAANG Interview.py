
Plane Maximum time in Air 
Input=[[2,5] ,[3,7],[8,9],[1,3]]

# Insert into a 2D array 
# for 1-24 , for every interval if plane exusts we count plane , and keep maximum track 

# data=[]

def InsertNewVal(data):
  output=[]
  for i,j in data:
    output.append((i,j))
  return output


def CountMaxInAir(data):
  count=0
  maxcount=0
  for i in range(0,23):
    count=0
    for start,end in data:
          # print('start',start)
          # print('end',end)
          # print('i',i)
          if start<=i<=end:
            count+=1
            print('count',count)
          maxcount=max(count,maxcount)
  return maxcount
