# "Identify underpaid managers/employees

# You are given a class representing employees, where each employee has a salary and a list of subordinates. The subordinates can further have their subordinates, forming a hierarchical employee structure. Given a root employee as input, write a program that lists employees who are managers and have a salary lower than the average salary of their subordinates.

# For example:

# - Emp1 (85k)
#     +- Emp2 (90k)
#         +- Emp3 (170k)
#         +- Emp4 (60k)
#     +- Emp5 (70k)
#         +- Emp6 (50k)
# In the provided example, since EMP2 has salary lower than the average of its subordinates, EMP3 and EMP4, EMP2 is considered an underpaid employee. Similarly, since EMP1 has salary lower than all of its subordinates, EMP1 is also classified as an underpaid employee."


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
Emp1.child=[Emp2,Emp5]
Emp2.child=[Emp3,Emp4]
Emp5.child=[Emp6]

# print(Emp1.name) # 85k 
# print(Emp4.salary) # Emp2 ,Emp5

# finding people whose salary average is less than direct peers 

# DFS 
# Step 1: finding peers calculating salary average , 
#         comparing and return if condition exists 
# moving to next Node untill we get no node 

# - Emp1 (85k)
#     +- Emp2 (90k)
#         +- Emp3 (170k)
#         +- Emp4 (60k)
#     +- Emp5 (70k)
#         +- Emp6 (50k)

def FindingUnderpaidEmployee(root,emps=[]):

    print(f'we are running for {root.name=}')  
    root_salary=root.salary  
    peer_count=0
    peer_average=0
    peer_salary=0

    for employees in root.child:

        print(f'we are running inside loop  {employees.name=}') 
        peer_salary+=employees.salary 
        peer_count+=1 
        peer_average= peer_salary//peer_count  
        FindingUnderpaidEmployee(employees,emps)

    if root_salary < peer_average and peer_average != 0:
        print(f'returning one guy')
        emps.append(root.name) 
    return emps


print(FindingUnderpaidEmployee(Emp1))
    