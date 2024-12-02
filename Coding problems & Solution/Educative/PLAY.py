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

List1=[(2,3),(3,4)]
print(f'before {List1=}')
List1=[(y,x) for x,y in List1]
print(f'After {List1=}')