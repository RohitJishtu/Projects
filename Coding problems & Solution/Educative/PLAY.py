# data=[[1,2],[3,4],[1,3]]



# # Put this data to a combined list 

# # list1=[]
# # list2=[]
# # for group in data:
# #     list1.append(group[0])
# #     list2.append(group[1])

# # print(f'{list1=}{list2=}')

# # # Now I want to create list with Trigger 


# # Combined_list=[]
# # for group in data:
# #     Combined_list.append(['start',group[0]])
# #     Combined_list.append(['End',group[1]])

# # print(f'{list1=}{list2=} {Combined_list=}')

# # Combined_list=sorted(Combined_list,key= lambda x:x[1])

# # print(f'{list1=}{list2=} {Combined_list=}')


# # Recusrion Practice 


# # factprial 

# # 5!

# # def factorial(number):
    
# #     if number==1:
# #         return 1 
    
# #     return number*factorial(number-1)

# # Fibonacchi up to number n 

# Input=5
# Array=[]


# def Fibonacchi(Input):
#     iter=0
#     def Fib_generator(Input,Array,index):

#         if iter==Input-1:
#             print('reached here ')
#             return Array

#         for index in range(1,Input):
#             if Input>1:
#                 print('reached here recursion ')
#                 prevNumber=Array[index]
#                 PrevNumber_1=Array[index-1]
#                 newnum=prevNumber+PrevNumber_1  
#                 Array.append(newnum)

#             Fib_generator(iter,Array,index)
#         return Array

#     Array=[]
#     if Input ==1:
#         Array=[0,1]
#         return Array
#     elif Input ==0:
#         Array.append(0)
#         return Array
#     else:
#         Array=[0,1]
#         return Fib_generator(Input,Array,0)
    

# # Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# # Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# # Analyze the time complexity (e.g., O(n)).1 word answer
# # Analyze the space complexity (e.g., O(n)).1 word answer
# # Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# # Give Optimised solution Code




# print(Fibonacchi(11))

# Array=input()
# limit=input()
# print(f'your Array {Array}')
# print(f'your Age {limit}')

# # Array,Limit=input.split(',')

# # print(f'Array {Array}')
# # print(f'Limit {Limit}')

# Experiments with Queue 


# from queue import deque
# Q1=deque()
# Q1.append(12)
# Q1.append(2)
# Q1.append(3)
# print(Q1)


# List Comprehension 

# List1=[(2,3),(3,4)]
# print(f'before {List1=}')
# List1=[(y,x) for x,y in List1]
# print(f'After {List1=}')

# maximum Planes in air 

# data=[[2,5] ,[3,7],[8,9],[1,3]]

# Answer=2

# Logic :

# Start= [2,3,8,1]
# End=[5,7,9,3]

# Start=[1,2,3,8]
# End=[3,5,7,9]

# # 24 times

# # for iter in :

# #     if iter= start:
# #         plane+1
# #     elif 
# #         iter in end 
# #         plane-1 
# #     maxp;ane=max(plane,maxplane)

# Logic 2 :

# data=[[2,5],[3,7],[8,9],[1,3]]


# def MaxAirPlanes(data):
#     maxAirplanes=0
#     Curr_maxAirplanes=0
#     mewlist=[]
#     for elements in data:
#         mewlist.append(('Start',elements[0]))
#         mewlist.append(('End',elements[1]))

#     # Sort the list 
#     mewlist=sorted(mewlist,key=lambda x:x[1])

#     for element in mewlist:
#         if element[0]=='Start':
#             Curr_maxAirplanes+=1
#         elif element[0]=='End':
#             Curr_maxAirplanes-=1
#         maxAirplanes=max(maxAirplanes,Curr_maxAirplanes)

#     return maxAirplanes

# print(MaxAirPlanes(data))

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# n=3 
# 1   2    3          4      5     6
# (   ()   ()         ()     ()    )
#     (    (          )       )
#     (    )          (      )
#     (    )          )       )       

# 1+2+2+2+2+1/2

# Program :
# n=6 , 3 p[en brackets , 3 closed brackets ina  list ]
# first position : open , close 

#     ( ( ( ) )) 
#     ( ) ( ) () 
#     ( ( ) ) ()

# ()()()

def MakeBrackets(n):
    brackets=[]
    for i in range(n//2):
        brackets.append('(')
        brackets.append(')')    

    combinations = (2 + ((n-2)*2)//2)
    result=[]
    for combination in range(combinations):
        ouput=''
        for item in range(len(brackets)):
            ouput += brackets[item]
            if item >0 and item < (len(brackets)-1):
                if brackets[item]=='(':
                   brackets[item]=')'
                else:
                   brackets[item]='('
            
        result.append(ouput)
    
        
    return result

print(MakeBrackets(6))

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code

# def MakeBrackets(n):
#     # Total pairs of parentheses
#     pairs = n // 2
#     # Stack to simulate recursion
#     stack = [("", 0, 0)]  # (current_string, open_count, close_count)
#     result = []

#     while stack:
#         current, open_count, close_count = stack.pop()
        
#         # If we've used all pairs, add to the result
#         if open_count == pairs and close_count == pairs:
#             result.append(current)
#             continue
        
#         # If open brackets can still be added
#         if open_count < pairs:
#             stack.append((current + "(", open_count + 1, close_count))
        
#         # If closing brackets can still balance the string
#         if close_count < open_count:
#             stack.append((current + ")", open_count, close_count + 1))
    
#     return result

# # Example Usage:
# print(MakeBrackets(6))  # For 6 brackets (3 pairs)

def MakeBrackets(n):
    # Total pairs of parentheses
    pairs = n // 2
    # Stack to simulate recursion
    stack = [("", 0, 0)]  # (current_string, open_count, close_count)
    result = []

    while stack:
        print(f'{stack=}')
        current, open_count, close_count = stack.pop()
        
        # If we've used all pairs, add to the result
        if open_count == pairs and close_count == pairs:
            result.append(current)
            continue
        
        # If open brackets can still be added
        if open_count < pairs:
            stack.append((current + "(", open_count + 1, close_count))
        
        # If closing brackets can still balance the string
        if close_count < open_count:
            stack.append((current + ")", open_count, close_count + 1))
    
    return result

# Example Usage:
print(MakeBrackets(6))  # For 6 brackets (3 pairs)
