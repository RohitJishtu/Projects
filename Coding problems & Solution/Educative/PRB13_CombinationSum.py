# I am not sure how many times 

Elements=[2,3,5]
Target=8 

# FindCombinatioNSum 


# Logic 

# 2 , keep adding 2 until I get 8 , if i get 8 -- i remove latest 
# go to next element and keep trying 

# if I get more than 8 , i go to next element 

# If I get less than 8 , I keep adding same element 


def CombinatioNSum(Elements,Target):
    Output=[]

    def backtrack (Elements,index=0,sum=0,temp=[],Output=[]):
        print(f'{temp=} {Output=} {index=} {sum=}')
        
        for i in range(index,len(Elements)):
            
            temp.append(Elements[i])
            sum+=Elements[i]

            if sum==Target:
                Output.append(temp.copy()) 
            
            elif sum<Target :
                backtrack (Elements,i+1,sum,temp,Output)

            temp.pop()
            sum-=Elements[i]

        return Output

    return backtrack(Elements)

print(CombinatioNSum(Elements,Target))