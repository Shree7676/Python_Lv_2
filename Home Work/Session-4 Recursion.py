"""
Homework questions

Ayman recently came to know that November 23rd is Fibonacci day because when written in mm/dd format as 11/23, 
these four numbers form a Fibonacci sequence. He got more interested in the Fibonacci sequence and finally decided 
to create a function in a python program to print the entire Fibonacci sequence. Write the same program in python 
and check how many terms are possible for you to print on the screen.
Note:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, …
This is the Fibonacci Sequence. It goes on infinitely and is made up of a series of numbers starting with 0, 
followed by 1, where each subsequent number is the sum of the previous two numbers.
Note: Use recursion to print the series.
"""
def fibo(n):
    
    if n <= 1 :
        return n
    
    return fibo(n-1) + fibo(n-2)

# main program 

terms = int(input("Enter the number of terms : "))

if terms < 0 :
    print("Please enter positive number")

else :
    for i in range(terms):
        print(fibo(i))



"""
The shopkeeper informed Chris that he is going to put this kind of offer on the daily basis. 
So Chris decided to write a python program and create a function that can find the number of 
chocolates that can be brought in different scenarios.
Write a program and create a function to find the answer with the help of recursion.
Note: The number of chocolates that can be bought depends upon three things, the money Chris has with him, 
the price of the chocolate, and number of wrappers are required to get the extra chocolate.
Sample explanation:
Input: money = 16, price = 2, wrap = 2
Output:   15
Price of a chocolate is 2. You can buy 8 chocolates from
amount 16. You can return 8 wrappers back and get 4 more
chocolates. Then you can return 4 wrappers and get 2 more
chocolates. Finally you can return 2 wrappers to get 1
more chocolate.
"""
def countExtraChocolates(chocolates , wrap):
    # chocolates - number of chocolates
    # wrap - number of wrappers required
    if chocolates < wrap :
        return 0
    
    extraChocolates = chocolates//wrap
    
    totalExtraChocolates = extraChocolates + chocolates%wrap
    
    return extraChocolates + countExtraChocolates(totalExtraChocolates , wrap)
    
def countChocolates(money , price , wrap):
    # money - total money 
    # price - price of each chocolate
    # wrap - number of wrappers required to get 1 extra chocolate
    chocolates = money//price
    
    extraChocolatesFromWrap = countExtraChocolates(chocolates , wrap)
    
    return chocolates + extraChocolatesFromWrap
# main program 
money = int(input("Enter the money you have : "))
price = int(input("Enter the price of each chocolate : "))
wrap = int(input("Enter the number of extra wrappers required to get 1 extra chocolate :"))

totalChocolates = countChocolates(money, price, wrap)

print(totalChocolates)