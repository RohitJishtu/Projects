# Making a binary tree , listing all elements in a binary tree 


class TreeNode():
  def __init__(self,data,left=None,right=None):

    self.data=data 
    self.left=left
    self.right=right



class CreateTree():
  def __init__(self,root):
    self.root=TreeNode(root)


  def PrintTree(self,root):
    # print(root.left)
    # print(root.right)
    if root.left:
       self.PrintTree(root.left)
      #  print('reaching printing left',root.left.data)
    print(f'{root.data=}')
    if root.right:
       self.PrintTree(root.right)
      #  print('reaching printing right',root.right.data)
  
  def PrintPreorder_Tree(self,root):
    # print(root.left)
    # print(root.right)
    print(f'{root.data=}')
    if root.left:
       self.PrintTree(root.left)
      #  print('reaching printing left',root.left.data)
    if root.right:
       self.PrintTree(root.right)
      #  print('reaching printing right',root.right.data)

  def InsertIntoTree(self,root,data):
    if root is None:
       print('reaching insertion with ')
       return(TreeNode(data))
    if data >= root.data:
      root.right=self.InsertIntoTree(root.right,data)
    else:
      root.left=self.InsertIntoTree(root.left,data)
    return root

  def DebthofTree(self,root):
    if root is None:
      return 0
    return max(self.DebthofTree(root.left),self.DebthofTree(root.right))+1


  def LevelOrderTraversal(self,root):
    
    Queue=[]
    LevelOrderMap={}
    Queue.append(root)
    j=0
    while len(Queue)>0:
        LevelOrderMap[j]=[]
        tempque=Queue
        Queue=[]
        loopvar=len(tempque)
        for iter in range(loopvar):
           print(f'{loopvar=}')
          #  print(f'{tempque=}')   
           Element=tempque.pop()
           print(f'{Element.data=}')
           LevelOrderMap[j].append(Element.data)

           if Element.left:
              Queue.append(Element.left)
           if Element.right:
              Queue.append(Element.right)
           print(LevelOrderMap)
        j+=1


    return Queue
        #    5
        #  /   \
        # 1    11
        #    /   \
        #   9     15
        #  / \      \
        # 7  13      24
  

Tree1=CreateTree(5)
print(Tree1.root)
Tree1.PrintTree(Tree1.root)
insertList=[1,11,9,7,15,24,13]

for i in insertList:
  Tree1.InsertIntoTree(Tree1.root,i)
Tree1.PrintPreorder_Tree(Tree1.root)
Tree1.LevelOrderTraversal(Tree1.root)

Tree1.PrintTree(Tree1.root)
Tree1.DebthofTree(Tree1.root)
