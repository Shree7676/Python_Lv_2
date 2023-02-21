#Creating dataframe datastructure

import pandas as pd
import numpy as np

ar=np.random.randint(0,100,(2,3))
print(ar)
df=pd.DataFrame(ar,index=["A","B"],columns=["P","Q","R"])
print(df)

dict={
    1:"hi",
    11:"hii",
    111:"hiii"
}
dict_to_df=pd.DataFrame(dict,index=[1,2,3])
print(dict_to_df)

list=[1,2,3,4,5,6]
listToDf=pd.DataFrame(list)
print(listToDf)

# /csv_Data/books.csv
csv=pd.read_csv("Class Work/csv_Data/books.csv")
csvToDf=pd.DataFrame(csv)
# print(csvToDf)
# print("*"*100)
# print(csvToDf.head())
# print("*"*100)
# print(csvToDf.tail())


#Series
print("*"*100)
print(csvToDf.columns)
print(csvToDf["Price"]*100)
print()
print(csvToDf[["Price","Year"]])
print(csvToDf["Price"][4])
print(csvToDf["Price"][0:5])


a=pd.Series([1,2,3,4],index=["a","b","c","d"])
b=pd.Series([1,2,3,4],index=["b","c","d","e"])
print(a.add(b,fill_value=0)) #or
print(pd.Series(a.values+b.values))



#CLASS WORK
print("*"*50,"CLASS WORK","*"*50)
"""
Shivam is analyzing the top 50 books sold on amazon. He is having data in the form of the CSV file ( books.csv ). Create a series of the price column and find the price of the book on row 20.
"""

print(csvToDf["Price"][20]) #or
prc=pd.Series(csvToDf["Price"])
print(prc[20])

"""
Shivam noticed that the prices of the book are now increased. So he wants to update the price of one book in the series of prices. He decided to increment the price of the book by $ 10. To help Shivam, update the price of a book on row 45.
"""
print(prc[45])
prc[45]=prc[45]+10
print(prc[45])

#HOME WORK
print("*"*50,"HOME WORK","*"*50)
"""
After working with the series of prices Shivam wants to extract some information about the ratings as well. Print the entire series of ratings and then find the rating of the book on row 76.
"""
rat=pd.Series(csvToDf["UserRating"])
print(rat)
print(rat[76])

"""
After looking at amazon Shivam found that the rating of a few books has been increased after getting a higher number of reviews. Write a program to update the rating of the books with the help of their index numbers to help Shivam in analyzing the series in a better way.
rating = [ 4.9 , 5.0 , 4.8 ] 
Index = [ 23 , 67 , 89 ]
"""

rating = [ 4.9 , 5.0 , 4.8 ] 
Index = [ 23 , 67 , 89 ]

rat.update(pd.Series([ 4.9 , 5.0 , 4.8 ],index = [ 23 , 67 , 89 ]))
# def updateRatings(arr_rat,arr_index):
#     for x in range(len(arr_index)):
#         print("OLD=",rat[arr_index[x]])
#         rat[arr_index[x]]=arr_rat[x]
#         print("NEW=",rat[arr_index[x]])

# updateRatings(rating,Index)