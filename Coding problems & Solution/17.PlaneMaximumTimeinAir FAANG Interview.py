
# Maximum Planes in Air 
# Input=[[2,5] ,[3,7],[8,9],[1,3]]

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


def MaxAirPlanes(data):
    maxAirplanes=0
    Curr_maxAirplanes=0
    mewlist=[]
    for elements in data:
        mewlist.append(('Start',elements[0]))
        mewlist.append(('End',elements[1]))

    # Sort the list 
    mewlist=sorted(mewlist,key=lambda x:x[1])

    for element in mewlist:
        if element[0]=='Start':
            Curr_maxAirplanes+=1
        elif element[0]=='End':
            Curr_maxAirplanes-=1
        maxAirplanes=max(maxAirplanes,Curr_maxAirplanes)

    return maxAirplanes

print(MaxAirPlanes(data))