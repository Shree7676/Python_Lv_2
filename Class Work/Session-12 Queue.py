"""
Enqueue: The Enqueue operation is used to insert the element at the rear end of the queue. It returns void.
Dequeue: It performs the deletion from the front-end of the queue. It also returns the element which has been removed from the front-end. It returns an integer value.
Peek: This is the third operation that returns the element, which is pointed by the front pointer in the queue but does not delete it.
Queue overflow (isfull): It shows the overflow condition when the queue is completely full.
Queue underflow (isempty): It shows the underflow condition when the Queue is empty, i.e., no elements are in the Queue.
"""

class Queue:

    def __init__(self,data) -> None:
        self.qu=[None]*data
        
    def Enqueue(self,data):
        if self.isfull() == False:
            self.qu.insert(0,data)
            self.qu.pop()


    def Dequeue(self):
        if self.isempty()==False:
            for x in range(len(self.qu)-1,-1,-1):
                if self.qu[x]!=None:
                    self.qu[x]=None
                    break
    
    def Peek(self):
        for x in range(len(self.qu)-1,-1,-1):
            if self.qu[x]!=None:
                return self.qu[x]

    def isfull(self):
        if None not in self.qu:
            return True     #this means its full
        else:
            return False

    
    def isempty(self):
        for x in self.qu:
            if x!=None:
                return False
        return True

q=Queue(5)
print(q.qu)
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue("ram")
q.Enqueue("Sham")
print(q.qu)
q.Dequeue()
print(q.Peek())
print(q.qu)