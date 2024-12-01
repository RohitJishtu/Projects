# Input: s = "abcabcbb"  
# Output: 3  
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"  
# Output: 1  
# Explanation: The answer is "b", with the length of 1.

# Input: s = "abcabcbb"  
# Output: 3  
# Explanation: The answer is "abc", with the length of 3.


# a b c a b c b b 

#     [a:0,b:1,c:3]

#  a  store in dictionary , length=3  , start =1 , end = 2
#  a  [already in dict     and position between start and end ] then reset  length=1 , start = 3 , end =current 
#  b  [already in dict     and position between start and end ] end++
#  c  end++
#  b  in dict between start and end  store max , else start=new , length=1 

s = "abcabcdbb"  
Output= 3  

# a=0 1 
# b=1 
# c=2


def LongSubstring(s):
    length=0
    maxlength=0
    start=0
    end=0
    map={}
    for chr in range(len(s)):

        if s[chr] not in map and (chr >= start):
            map[s[chr]]=chr
            length+=1
            end+=1
        else:
            start=chr
            end=start
            length=1

        print(f'{length=} {map=} {maxlength=} {start=} {chr=}')
        maxlength=max(length,maxlength)
    
    return maxlength

print(LongSubstring(s))

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code
