# Problem statement
# You are given two strings 'STR1' and 'STR2'. You need to tell whether the strings are meta strings or not.
# Meta strings are strings that can be made equal by swapping exactly one pair of distinct characters in one of the strings.

# Note:
# Equal strings are not considered as meta strings. 

# Coding
# Codnig

# Play
# Playes

from collections import Counter


string1= "Coding"
string2= "Codni"

def MetaStrings(string1,string2):
    dictstring1={}
    for i in string1:
        if i in dictstring1:
            dictstring1[i]+=1
        else :
            dictstring1[i]=1
    dictstring2={}
    for i in string2:
        if i in dictstring2:
            dictstring2[i]+=1
        else :
            dictstring2[i]=1

    if dictstring1 ==dictstring2:
        return True
    return False 

    
print(MetaStrings(string1,string2))