# Python Code for Top K Frequent Elements:
# 2th Frequent element 
# Approach 1 : Counter n + nlogn +k 
#              Dict Inseryion + Sorting + finding kth 
# Approach 2: Counter + Heapify (o(n)) + Extraction logn = O(n )

from collections import Counter 
import heapq

List1=[1,2,1,1,3,4,1,6,7,7,9,1]
k=1

def MakeCounter(List):
    return Counter(List)


Map={}
Map=MakeCounter(List1)
heap=list(Map.items())

for idx, iter in enumerate(heap):
    # Extract the values i and j
    i, j = iter
    # Swap the values in place and update the tuple in the heap
    heap[idx] = (j, i)  # Swap i and j inside the tuple


print(f'{heap=}')

heapq.heapify(heap)

for i in range(k):
    if i==k-1:
        print(heap[i])
    heap.pop()

