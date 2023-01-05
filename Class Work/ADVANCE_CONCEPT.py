#Dictionaries
# p={"AAPL":612.78,"ACME":45.23,"IBM":205.55,"HPQ":3,"FB":10.7}

# a=min(p,key=lambda x:p[x])      ################## VERY GOOD #####################





# a={
#     "x":1,
#     "y":2,
#     "z":3
# }
# b={
#     "w":10,
#     "x":11,
#     "y":2
# }
# print(a.keys() - b.keys()) # will return uncommon items of a 
# print(a.keys() & b.keys()) # will return common keys
# print(a.items() & b.items()) # will return common item in dic





# # __ use of yield
# def fnc():
#     for x in range(1,21):
#         if x%2==0:
#             yield x   # return will stop in first encounter while yield goes on accumalating data

# even=fnc()
# for x in even:
#     print(x)





# arr=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# arr[3::2]=["x","y","a","b"]
# print(arr[3::2])
# print(arr)

# from collections import Counter
# lis=[1,2,3,4,5,6,5,4,5,1,1,1,5]
# word=Counter(lis)
# top=word.most_common(2)
# print(top)
# print(word[1]) # >> 4
# print(word) # >> Counter({1: 4, 5: 4, 4: 2, 2: 1, 3: 1, 6: 1})


# --------------------sorting a dic by required keys-------------------------- #

# from operator import itemgetter

# lis=[
#     {"fName":"Shree","lName":"Nandi","id":1},
#     {"fName":"apple","lName":"xyz","id":2},
#     {"fName":"ball","lName":"abc","id":9},
#     {"fName":"zebra","lName":"pqr","id":7},
# ]

# row_fName=sorted(lis,key=itemgetter("fName"))
# row_id=sorted(lis,key=itemgetter("id"))
# # or second Method
# row_lName=sorted(lis,key=lambda l:l["lName"])

# print(row_fName)
# print(row_id)
# print(row_lName)