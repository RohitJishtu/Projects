# "Identify underpaid managers/employees

# You are given a class representing employees, where each employee has a salary and a list of subordinates. The subordinates can further have their subordinates, forming a hierarchical employee structure. Given a root employee as input, write a program that lists employees who are managers and have a salary lower than the average salary of their subordinates.

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
# Emp7 = TreeNode('Emp7',100)
Emp1.child=[Emp2,Emp5]
Emp2.child=[Emp3,Emp4]
Emp5.child=[Emp6]
# Emp6.child=[Emp7]

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


def FindHLevels(root,maxlevel=0):
    print(f'we are in {root.name=}')
    level=0
    if root is None:
        return  level
    for emps in root.child:
        print(f'we are in childs {emps.name=}')
        level=FindHLevels(emps,maxlevel)  
        maxlevel=max(level,maxlevel)
        
    level+=1
    print(f'level is updated to {level=}')
    return level 

print(FindHLevels(Emp1))