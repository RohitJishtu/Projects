Ques [
  # Identify underpaid managers/employees

# You are given a class representing employees, where each employee has a salary and a list of subordinates.
# The subordinates can further have their subordinates, forming a hierarchical employee structure.
# Given a root employee as input, write a program that lists employees who are managers
# and have a salary lower than the average salary of their subordinates.

# For example:

# - Emp1 (85k)
#     +- Emp2 (90k)
#         +- Emp3 (170k)
#         +- Emp4 (60k)
#         +- Emp41 (50k)
#     +- Emp5 (70k)
#         +- Emp6 (50k)


# In the provided example, since EMP2 has salary lower than the average of its subordinates,
# EMP3 and EMP4, EMP2 is considered an underpaid employee.
# Similarly, since EMP1 has salary lower than all of its subordinates,
# EMP1 is also classified as an underpaid employee.


  #            E1

  #     E2              E5

  # E3.  E4. E41      E6

]

class employees:
    def __init__(self,name=None,sal=None,SubOrd=None):
      self.name=name 
      self.salary=sal
      self.SubOrd= SubOrd if SubOrd is not None else []

    def printSubOrd(self,emp):
      for i in emp.SubOrd:
        print(i.name)
        self.printSubOrd(i)

    def AvgSubOrd_Salary(self,emp,sumsal=0,count=0):

      # print(f'running with {emp.name=},{sumsal=},{count=}')
      for i in emp.SubOrd:
        sumsal+=i.salary
        count+=1
        sumsal,count=self.AvgSubOrd_Salary(i,sumsal,count)
      
      return sumsal,count


E1=employees('E1',85,[])
E2=employees('E2',90,[])
E5=employees('E5',70,[])
E1.SubOrd=[E2,E5]
E3=employees('E3',170,[])
E4=employees('E4',60,[])
E41=employees('E41',50,[])
E2.SubOrd=[E3,E4,E41]
E6=employees('E6',70,[])
E5.SubOrd=[E6]


ObjectList=[E1,E2,E5,E3,E4,E41,E6]
for i in ObjectList:
  sum,count=E1.AvgSubOrd_Salary(i)
  if count >0:
    print('sum,count',sum,count,sum/count,E1.salary)
    if i.salary <= sum/count:
      print('manager Less=',i.name)
    else:
      print('manager Okay=',i.name)


