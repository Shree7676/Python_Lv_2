#Homework questions
"""
Shubham is a classmate of Nidhi, and he is also preparing for the examination. He also wants to revise the topics after learning everything but in the same order instead of reverse order. Create a function reverseStack() that can reverse the entire stack from top to bottom. In this way, Shubham will be able to use the stack for his preparation.
Hint: reverse the stack using two extra temporary stacks.
"""

class stack:

    def __init__(self,limit) -> None:
        self.stak=[None]*limit

#reverseStack()
    def reverseStack(self):
        temp1=stack(len(self.stak))

        for x in range(len(self.stak)-1,-1,-1): # runs in reverse order .... Efficient will work with just 1 temp stash
            if self.stak[x]!=None:
                temp1.push(self.stak[x])

        self.stak=temp1.stak

    def push(self,data):
        if self.isEmpty:
            self.stak.append(data)
            self.stak.pop(0)
        else:
            self.isFull
    
    def pop(self):
        if self.stak[-1]!=None:
            self.stak.pop()
            self.stak.insert(0,None)
    
    def isEmpty(self):     #it should be complete empty 1/2 full not allowed
        for x in self.stak:
            if x!=None:
                return False
        return True
    
    def isFull(self):
        if None not in self.stak:
            return True
        return False
    
    def peek(self,index=-1):
        return self.stak[index]
    
    def count(self):
        c=0
        for x in self.stak:
            if x!=None:
                c+=1
        return c
    
    def change(self,index,data):
        self.stak[index]=data
    
    def display(self):
        for x in self.stak: print(x)

obj=stack(5)
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.stak)
obj.reverseStack()
print(obj.stak)

"""
Abhinav completed his project successfully and now he started analyzing a new stock. He has stock prices for the past 45 days. He wants to check how many times the stock made an all-time high in a form of a list. He has a list of historical prices. Write a python program to convert the list into such a form that can easily represent days when the stock made an all-time high.
Hint: Using STACK for each element in the stock, find out the greatest element to the left and change the value to that. If there is no greatest element to the left then make the element -1 and that will represent a day when the stock made all time high. 

Example: 
List of historical price:
[ 498 , 536 , 520 , 512 , 543 , 555 , 560 , 551 ]
List which shows the days when the stock made an all-time high:
[ -1 , -1 , 536 , 536 , -1 , -1 , -1 , 560 ]
Note: As an example, you can create a list of 33 random numbers in a particular range or take the input.
"""

