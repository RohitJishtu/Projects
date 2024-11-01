import pandas as pd
print("TEST")


# Download latest version
data=pd.read_csv('books.csv',on_bad_lines='skip')
# print(data.head)

# Q1 : Finding Duplicates 

columnslist=list(data.columns)
print(columnslist)


def FindDuplicates(data,keyslist):
    Group=data.groupby(keyslist).size().reset_index(name='counts')
    count=0
    # for record in Group["counts"]:
    #         if record >1:
    #               count+=1 
    count = Group[Group['counts'] > 1].shape[0]
    
    return count 

keyslist=['authors','title','publisher']
# print(FindDuplicates(data,keyslist))


# Q1 : Finding Author with maximum books 

group=data.groupby(['authors'] ).size().reset_index(name='books')
max_books_author = group.loc[group['books'].idxmax()]
# print(max_books_author)

#Q3:  Read csv files without pands 
import csv 
filepath='books.csv'
# data=read_csv(filepath)

with open(filepath,mode='r') as file:
    csv_reader=csv.reader(file)
    for row in csv_reader:
            data.append(row)
print(data)