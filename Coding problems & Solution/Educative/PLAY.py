data=[[1,2],[3,4],[1,3]]



# Put this data to a combined list 

list1=[]
list2=[]
for group in data:
    list1.append(group[0])
    list2.append(group[1])

print(f'{list1=}{list2=}')

# Now I want to create list with Trigger 


Combined_list=[]
for group in data:
    Combined_list.append(['start',group[0]])
    Combined_list.append(['End',group[1]])

print(f'{list1=}{list2=} {Combined_list=}')

Combined_list=sorted(Combined_list,key= lambda x:x[1])

print(f'{list1=}{list2=} {Combined_list=}')