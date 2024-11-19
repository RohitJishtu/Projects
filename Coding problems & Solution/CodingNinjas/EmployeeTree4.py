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


# In the below tree give me left visible nodes only 

#                 E1            1 

#         E2              E5    2     [E3,E4,E5]

# E3              E4          E6 3   [E7]

#                                 E7

# left visible : E1 , E2 ,E3 ,E7


# for every level the first node should be displayed using BFS 
# Start from root , add root , go for childs 
# # Add first child , go for childs 
# if no child , go for second until we find child and we keep going to klast 

from collections import deque
def LeftVisible(root,level=1,leftvisible=[]):   
    nodes=deque()
    nodes.append(root)
    leftvisible.append(root.name)
    newchilds=deque()
    levelfirst=0
    while len(nodes)>0:
        current_node=nodes.popleft()
        for child in current_node.child:
            if levelfirst==0:
                leftvisible.append(child.name)
                levelfirst=1
            newchilds.append(child)
        print(f'{leftvisible=} {len(newchilds)=}')
        if len(nodes)==0:
           nodes=deque()
           nodes=newchilds
           newchilds=deque()
           levelfirst=0
    return leftvisible

print(LeftVisible(Emp1))


Ques =  {
          Please Rate my above written [Code].
          Give me rating out of 5 with respect to interviews. 
          Give Time complexity 
          Give Space complexity 
          Also list down Coder's stregths and weaknesses 
          Add Comments for the code , dont change anything in the code 
        }

