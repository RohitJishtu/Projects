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


def Fibo(k,array=[0,1]):
  if len(array) >=k:
    return array
  array.append(array[-1]+array[-2])
  Fibo(k,array)

 
  return array 



