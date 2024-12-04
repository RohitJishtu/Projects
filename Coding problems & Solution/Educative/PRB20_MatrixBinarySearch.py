matrix = [[1,2,3],
          [4,5,6],
          [7,8,9] 
         ]
Serach_element=8
rows_len= len(matrix)
cols_len= len(matrix[0])
print(f'{rows_len=} {cols_len=}')

# search element in matrix 

def BinarySerach(array,low,high,Serach_element):
      print(f'{low=},{high=}')
      while low < high:
        mid = low+high//2
        if array[mid]==Serach_element:
                return mid 
        elif array[mid]>=Serach_element:
                right=right-1
        else:
                left=left+1
        return None       

# Linear serach 

for row in range(rows_len):
        # Binary Serach 
        low_val =matrix[row][0]
        high_val=matrix[row][cols_len-1]

        if low_val<Serach_element<high_val:
            elementpos=BinarySerach(matrix[row],0,cols_len-1,Serach_element)
            if elementpos:
                print(f'{Serach_element} is at position {row,elementpos=}') 
                break 



# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
# Give Optimised solution Code

