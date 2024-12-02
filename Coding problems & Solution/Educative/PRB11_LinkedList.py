# There is a List with address to next ,ocation given , you need to revrese the lisyt 




class LinkedNode:
    def __init__(self,data,next=None):
        self.data=data 
        self.next=next 

Node1 = LinkedNode(1)
Node2 = LinkedNode(2)
Node3 = LinkedNode(4)
Node4 = LinkedNode(5)
Node5 = LinkedNode(3)
Node6 = LinkedNode(7)
Node1.next=Node2
Node2.next=Node3
Node3.next=Node4
Node4.next=Node5
Node5.next=Node6


class Linkedlist:

    def __init__(self,head):
        self.head=head

    def ReverseList(self):
        curr=self.head                   
        prev=None
        temp=None
        while curr:
            temp=curr               
            if curr.next:
                curr=curr.next 
            else:
                curr=None
            temp.next=prev
            prev=temp 
            # print(f'{curr.data=} {temp.data=} {prev.data=} ')
        self.head=temp
        return 

    def PrintList(self,head):
        List=[]
        while head:
            List.append(head.data)
            head=head.next 
        return List



         
# List1=     None < [[1]  2 > 4> 5 > 3 >7 ]
        #   head      
# Insertion in linked list 



LL1=Linkedlist(Node1)
print(f'before {LL1.PrintList(Node1)}')
LL1.ReverseList()
print(LL1.PrintList(Node1))
print(f'after {LL1.PrintList(Node6)}')


# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code

