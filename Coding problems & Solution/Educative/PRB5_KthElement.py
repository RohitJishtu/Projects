# You are given a list find the Kth Lowest element in the list , without sorting 
# Using Heapsort 
# Q1: Will be the entire array be sorted 
# heapify the Array 
# min heap 


List1=[1,2,5,6,7,3,4]
k=6
Answer=4

print(f'{List1=}')
import heapq
heapq.heapify(List1)
for i in range(k):
    print(f'{i=} {List1=}')
    if i==k-1:
        print(List1[0])
    heapq.heappop(List1)

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code

