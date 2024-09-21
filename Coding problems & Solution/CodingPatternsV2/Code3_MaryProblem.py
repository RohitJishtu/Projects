# # maximum possible number of different types of candy that Mary can eat after she has given uniique N/2 candies to her brother.

# # Example 1 
# # candies = [3, 4, 7, 7, 6, 6]
# # candies_remaining = [3, 7, 6]  (3)

# # Example 2
# # candies = [80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]
# # candiesremaining= [1000000000, 123456789, 80, 80, 80] (3)



# candies = [3, 4, 7, 7, 6, 6]
# candies_remaining = [3, 7, 6]  

# 3: 1 
# 4: 1
# 7: 2
# 6: 2


# UniqueCandies = 3,4,7,6
AllCandies = [1, 2, 3, 4, 5, 6]
UniqueCandies=set(AllCandies)


def FIndUnique_remaining(AllCandies,UniqueCandies):
    giveaway=len(AllCandies)//2
    print(f'{giveaway=}')
    if giveaway <= len(AllCandies)-len(UniqueCandies):
        return len(UniqueCandies)
    else:
        giveaway-=(len(AllCandies)-len(UniqueCandies))
        Counter=len(UniqueCandies)
        for counter in range(len(UniqueCandies)):
            print(f'{Counter=}')
            if giveaway==0:
                return Counter
            else:
                giveaway-=1
                Counter-=1

print(FIndUnique_remaining(AllCandies,UniqueCandies))


# set = [3,4,7,6]
# if setval in list:
# values = [1,1,2,2] 
# keys=[3,4,7,6]
# numbers=[0,1,2,3]
# giveaway= len(candies)//2