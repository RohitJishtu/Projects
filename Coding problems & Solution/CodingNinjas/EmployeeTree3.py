# For example:

# - Emp1 (85k)
#     +- Emp2 (90k)
#         +- Emp3 (170k)
#         +- Emp4 (60k)
#     +- Emp5 (70k)
#         +- Emp6 (50k)



class TreeNode:
    def __init__(self,root,salary=None,child=[]):
        self.name = root 
        self.salary=salary
        self.child =[]

# Inserting Data to root 

Emp1 = TreeNode('Emp1',85)
Emp2 = TreeNode('Emp2',90)
Emp3 = TreeNode('Emp3',170)
Emp4 = TreeNode('Emp4',60)
Emp5 = TreeNode('Emp5',70)
Emp6 = TreeNode('Emp6',50)
Emp7 = TreeNode('Emp7',100)
Emp1.child=[Emp2,Emp5]
Emp2.child=[Emp3,Emp4]
Emp5.child=[Emp6]
Emp6.child=[Emp7]

# print(Emp1.name) # 85k 
# print(Emp4.salary) # Emp2 ,Emp5

# finding how many hierarchi levels are there 

# every debth we count as one and thats all , we do itfor every branch 
# when I go both sides I pick max 

# - Emp1 (85k)              3   
#     +- Emp2 (90k)         2
#         +- Emp3 (170k)    1
#         +- Emp4 (60k)     1
#     +- Emp5 (70k)         2
#         +- Emp6 (50k)     1


# Finding Average at a particular level (BFS) 
# left side traversal 

# traverse the tree : store data in queue and then iterate through the childs , getying values and then 

# root > value , root.child1 > value root.child2 > value  average , then go from child one onwards as its next in queue 

# root - insert , iterate queue  1:root 
#     childs - insert -iterate queue 2: childs 
#         go down 3:childs and child;s childs 


# - Emp1 (85k)              3   
#     +- Emp2 (90k)         2
#         +- Emp3 (170k)    1
#         +- Emp4 (60k)     1
#     +- Emp5 (70k)         2
#         +- Emp6 (50k)     1

from collections import deque
def AverageAtlevel(root,Average={},nodes=deque(),level=1):
    sum=0
    nodes.append(root)  
    while  len(nodes) >0 :
        count=0
        sum=0
        gchilds=[]
        allnodes=len(nodes)  
        print(f'{allnodes=} {Average=}')  #Emp2,Emp3 ,[Emp3,Emp4,Emp6]
        for child in range(allnodes):
            sum+=nodes[child].salary
            count+=1
            if len(nodes[child].child)>0:
                for grandchild in nodes[child].child:
                    nodes.append(grandchild)
        for i in range(allnodes):
            nodes.popleft()  
        if level not in Average:
            Average[level]=sum/count
        level+=1
    return Average 

print(AverageAtlevel(Emp1))



Ques =  {
          Please Rate my above written [Code].
          Give me rating out of 5 with respect to interviews. 
          Give Time complexity 
          Give Space complexity 
          Also list down Coder's stregths and weaknesses 
          Add Comments for the code , dont change anything in the code 
        }

