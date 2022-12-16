
"""
Homework questions 
Kunal wants to create a password for his social media account. For his password, he wants to use only characters that occur in his name. He wants to use the characters K, U, N, A, and L. He wondered how many possible passwords are there if the length of the password can be anything with no repetition of characters. Write a python program and use recursion to find the answer of the same question. Also, check how many passwords are possible with the characters of your name. Print all the passwords on the screen.
"""

l=["k","u","n","a","l"]

def comb(l):
    if len(l)==0:
        return [[]]
    co=[]
    r=comb(l[1:])
    for c in r :
        co += [c,c+[l[0]]]
    return co

print(comb(l))

"""
Himanshi and Arunima were returning from school. On the school bus, they were playing a game. They were calculating the sum of all the digits of a vehicle number of the vehicles overtaking their bus. Arunima reached home and she thought she can create a program that can calculate the sum of all digits of a given number. But she doesn’t want to use string manipulation. Write a python program to find the sum of all the digits of a given number and print it on the screen to help Arunima.
"""
num=int(input("enter any num"))
def sum_of_all(num):

    if len(str(num))==1:
        return num
    sum=sum_of_all(num//10)+num%10
    return sum
print(sum_of_all(num))


