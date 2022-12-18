"""
push(): When we insert an element in a stack then the operation is known as a push. If the stack is full then the overflow condition occurs.
pop(): When we delete an element from the stack, the operation is known as a pop. If the stack is empty means that no element exists in the stack, this state is known as an underflow state.
isEmpty(): It determines whether the stack is empty or not.
isFull(): It determines whether the stack is full or not.'
peek(): It returns the element at the given position.
count(): It returns the total number of elements available in a stack.
change(): It changes the element at the given position.
display(): It prints all the elements available in the stack.
"""
#stack LIFO

class stack:

    def __init__(self,limit) -> None:
        self.stak=[None]*limit

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
obj.push(1)
obj.push(1)
obj.push(1)
print(obj.stak)
print(obj.isEmpty())
print(obj.isFull())
print(obj.count())
obj.push(1)
obj.push(1)
print(obj.stak)
print(obj.isEmpty())
print(obj.isFull())
print(obj.count())

"""
Nidhi is preparing for her examination, and she has so many topics to cover. She decided to study each topic properly, and then revise each topic in reverse order to finalize it. To make her work easy, write a python program and create a Stack class ( stack data structure ) where she can add the topic that she is learning for the first time. After completing all the topics she can check the peak value of the stack to check which topic she has to revise. After revising the topic she can pop the element from the stack. Once the stack becomes empty, it indicates she is ready for her examination.
"""
# using above stack itself ... just creating the object

Nidhi=stack(6) #she has 6 subjects
Nidhi.push("math") #adding the sub that she learnt
Nidhi.push("eng") #adding the sub that she learnt
Nidhi.push("sci") #adding the sub that she learnt
Nidhi.push("python") #adding the sub that she learnt
Nidhi.peek() # to check which is the first sub to revise

Nidhi.pop()  
Nidhi.pop()  

print(Nidhi.stak)  

"""
Abhinav is working on his data visualization project. He is analyzing a stock, and one of the columns in his data is stock span. He is having all the historical prices of stock in a list and somehow he wants to extract the stock span for each day. Write a python program to create a list of stock span using the given list of historical prices.
Hint: Use stack 
Note: Given a list of rates of a certain stock for some number of days, the stock span​ is the number of consecutive days (before a specific day) when the price of the stock was less than or equal to the price on this specific day.
"""
#100,80,60,70,60,75,85 >> 1,1,1,2,1,4,6
#10, 4, 5, 90, 120, 80 >> 1 1 2 4 5 1

# Without stack solution- Method 1 (not optimal solution)

l=[10, 4, 5, 90, 120, 80]
span=[]
for x in range(len(l)):
    c=1
    for y in range(x,-1,-1):
        if l[x]>l[y]:
            c=c+1
        elif l[x]<l[y]:
            break
    span.append(c)

print(span)


# implementing stack - Method 2

data=[100,80,60,70,60,75,85 ]  #1 1 2 4 5 1
stock=stack(len(data))
ans=[]
for x in range(len(data)):
    while (stock.isEmpty() is not True ) and stock.peek()<data[x]:
        stock.pop()
    if stock.peek()==data[x-1] :
        ans.append(1)
    else:
        ans.append(x-(stock.count()-1))
    stock.push(data[x])

print(f"cool it worked {ans}" )


