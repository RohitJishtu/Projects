
# Let's consider the following infinite sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, 12, 7, 10, 8, 9, ...
# The 0th element is 0 and the 1st element is 
# 1. The successive elements are defined recursively. Each of them is the sum of the separate digits of the
# two previous elements.
# Write a function:
# def solution(n)
# that, given an integer
# `
# n
# `
# , returns the
# `
# n
# `
# -th element of the above sequence.
# Examples:
# 1. Given n = 2, the function should return 1.
# 2. Given n = 6, the function should return 8.
# 3. Given n = 10, the function should return 10.
# Write an efficient algorithm for the following assumption:
# -
# `
# n
# ` is an integer within the range [0..1,000,000,0
# Fibonacci Sequence up to n 
# Step 1 :Generate the ItemSequenceNo , Sum 
#         n-2 , n-1 , n 
#         return n , only if n==input 


# 0, 1, 1, 2, 3, 5, 8, 13, 12, 7, 10, 8, 9, ...
findthis=8

def Fibonacci(findthis,NMinus_2=0,NMinus_1=1,SEQ_N=2):

    if findthis==0:
        return 0 
    if findthis==1:
        return 1
    
  

    NMinus_2_Sum=0
    NMinus_1_Sum=0

    if len(str(NMinus_2)) >1 : 
        for i in str(NMinus_2):
            NMinus_2_Sum+=int(i)
    else:
        NMinus_2_Sum=NMinus_2
    if len(str(NMinus_1)) >1 :
        for i in str(NMinus_1):
            NMinus_1_Sum+=int(i)
    else:
        NMinus_1_Sum=NMinus_1
    N= NMinus_2_Sum+NMinus_1_Sum
    print(f'Numbers calling are {NMinus_2=},{NMinus_1=} {N=} {SEQ_N}')

    if findthis==N:
       print('here',N)
       return SEQ_N
    return Fibonacci(findthis,NMinus_1_Sum,N,SEQ_N+1)

print(Fibonacci(8))



 