newlist=[1,2,2,3,1,4,4,4,5,6]
k=3
# Give me first highest frequence and 3rd higest frequency 

from collections import Counter
from collections import defaultdict

map=defaultdict(int)
map=Counter(newlist)
map={1:2,2:2,3:1,4:3,5:1,6:1}


newlist2=[(key,val) for key,val in map.items()]

print(newlist2)

import heapq
from heapq import heapify 
heap=[]

# Push elements into heap 


for element in newlist2:
    heapq.heappush(heap,(element[1],element[0]))

print(f'Approach 2 {heap=}')
      
for times in range(k-1):
    heapq.heappop(heap)

print(f'result2 {heap.pop()=}')