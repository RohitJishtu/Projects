
Array=[1,2,5,4,3,6]

# Sort Using Heap Sort 
# Heapifying : O(n) + O(nlogn)

from heapq import heapify,heappop


def Customer_heapify(Array):

    pass




def HeapSort(Array):
    heapify(Array)
    SortedList=[]
    for i in range(0,len(Array)):
        SortedList.append(heappop(Array))

    return SortedList

print(HeapSort(Array))


Array=[1,2,5,4,3,6]

        #             1 
        #     2             5
        # 4       3    6   