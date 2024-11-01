# Question : Can you make a Employee and Manager Tree based on below data along with their Salaries 
# Employes Manager Salary 
#     A      K        100
#     B      K        200
#     C      K        150
#     D      C        100
#     E      C        120
#     G      A        120
#     F      A        250
#     K      null     

# Q1 : Find the people reporting to Input Employees 

import logging
logging.basicConfig(level=logging.INFO)  # This will show INFO and higher-level messages
logging.info('Class Created')


class Employees:
	def __init__(self , Name , Salary=None , Manager=None):
		self.Name=Name 
		self.Salary=Salary 
		self.Manager=Manager 
		self.reportees=[]
	def __repr__(self):
		return (f'{self.Name=} {self.Manager=} {self.Salary=}')
	

class EmpTree:
	def __init__(self,root):
		self.root=root
	def Count_DirectReportees(self,Node,currentroot=None):
		print(f'Start {currentroot=}')
		if currentroot is None :
			currentroot=self.root
		if Node.Name==currentroot.Name:
			print('inside if =',len(currentroot.reportees))
			return len(currentroot.reportees)
		else:
			print(f'{currentroot=}')
			for element in currentroot.reportees:
				if self.Count_DirectReportees(Node,element):
					return  self.Count_DirectReportees(Node,element)
				else:
					continue
	def Levelsin_Company(self,CEO,level=0):
		if len(CEO.reportees)==0:
			return 1
		for reportees in CEO.reportees:
				print(f'{reportees=} {level=} {len(CEO.reportees)=}')
				level+=self.Levelsin_Company(reportees,level)	
		return level
		 
        # out of all Tree Members if Manager is Name then List them out 


A= Employees('A',100,'K')
B= Employees('B',200,'K')
C= Employees('C',150,'K')
D= Employees('D',100,'C')
E= Employees('E',120,'C')
G= Employees('G',120,'A')
F= Employees('F',250,'A')
K= Employees('K',250)

        #             k 
					
        #     A        B          C 

        # g     f             D       E
Tree1=EmpTree(K)
K.reportees=[A,B,C]
A.reportees=[G,F]
C.reportees=[D,E]
# print(Tree1.Count_DirectReportees(C))

print(Tree1.Levelsin_Company(K))
