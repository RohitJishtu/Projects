# You are given a tree and required to :

# 1. Insert Employees and Managers in Tree 
# 2. Find Debth of Tree using DFS and BSF 
# 3. Create a BST and insert Elements in Tree 
# 4. Invert a binary Tree 


# - Emp1 (85k)
#     +- Emp2 (90k)
#         +- Emp3 (170k)
#         +- Emp4 (60k)
#     +- Emp5 (70k)
#         +- Emp6 (50k)

class TreeNode:
    def __init__(self,Name,Salary=None,Subordinates=[]):
        self.name=Name 
        self.salary=Salary 
        self.subordinates=Subordinates

Emp1=TreeNode('Emp1',85)
Emp2=TreeNode('Emp2',90)
Emp3=TreeNode('Emp3',170)
Emp4=TreeNode('Emp4',60)
Emp5=TreeNode('Emp5',70)
Emp6=TreeNode('Emp6',50)

Emp1.subordinates=[Emp2,Emp5]
Emp2.subordinates=[Emp3,Emp4]
Emp5.subordinates=[Emp6]





class EmpTree:
    def __init__(self,root):
        self.root=root


    def DFS_FindEmp(self,root,Emps=[]):
        if root==None:
            return 
        Root_Salary=root.salary
        subord_salary=0
        count=0
        Average_Sub=0
        #Average Subordinate salary 
        for sub in root.subordinates:
            subord_salary+=sub.salary
            count+=1
            self.DFS_FindEmp(sub,Emps)
        
        if count>0:
            Average_Sub= subord_salary/count 
            if Average_Sub>Root_Salary:
                Emps.append(root.name)
        print(f'{root.name=} {count=} {Emps}')
        return Emps


    def BFS_FindEmp(self,root,Emps=[]):
        from queue import deque
        Q1=deque()
        Q1.append(root)
        while Q1:
            currentnode=Q1.popleft()
            Root_Salary=currentnode.salary
            subord_salary=0
            Average_Sub=0
            childlist=[]
            count=0
            for sub in currentnode.subordinates:
                 subord_salary+=sub.salary
                 count+=1
                 childlist.append(sub)
                #  print(f'{currentnode.name=} {sub.name=} {subord_salary=} {count=}')
           
            if count>0:
                Average_Sub= subord_salary/count 
                print(f'{Average_Sub=} {Root_Salary=}')
                if Average_Sub>Root_Salary:
                    Emps.append(currentnode.name)
                    print('emps array',Emps)
            if len(Q1)==0:
                for child in childlist:
                    Q1.append(child)  
        return Emps    

# - Emp1 (85k)
#     +- Emp2 (90k)
#         +- Emp3 (170k)
#         +- Emp4 (60k)
#     +- Emp5 (70k)
#         +- Emp6 (50k)
  
 
    def FindMaximumDebth(self,root):
        from queue import deque
        Q2=deque()
        Q2.append(root)
        currentlelevl=1
        childlist=[]
        while Q2:
            current=Q2.popleft()
            for sub in current.subordinates:
                childlist.append(sub) 
            if len(Q2)==0:
                for child in childlist:
                    Q2.append(child)  
                currentlelevl+=1
        return currentlelevl
    
# - Emp1 (85k)
#     +- Emp2 (90k)
#         +- Emp3 (170k)
#         +- Emp4 (60k)
#     +- Emp5 (70k)
#         +- Emp6 (50k)
  
    
    def DFS_FindMaximumDebth(self,root):
        
        if root is None:
            return 1
        
        for sub in root.subordinates: 
            d=1
            d+=self.DFS_FindMaximumDebth(sub)



Tree1=EmpTree(Emp1)


print(Tree1.FindMaximumDebth(Emp1))

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code
