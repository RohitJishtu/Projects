# 242. Valid Anagram
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false



s="aacc"
t="ccac"

class Solution:
    def isAnagram(s: str, t: str) -> bool:
    
        if len(s)!=len(t):
          return False 

        word1={}
        word2={}
        for i in s:
          if i not in word1:
            word1[i]=1
          else:
            word1[i]+=1

        for j in t:
          if j not in word2:
            word2[j]=1
          else:
            word2[j]+=1

        if word1!=word2:
          return False 

        return True 
Solution.isAnagram(s,t)

