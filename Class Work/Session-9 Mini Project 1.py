"""
●	Anisha is learning statistics and she is unable to find the values of central tendency
( Mean, Median, and Mode) correctly. To help her write a python program. Create a class ct ( central tendency )
that will store the list of values. Then create 5 methods:
●	addValue()
●	removeValue()
●	mean()
●	median()
●	mode()
●	Note:
●	To find mean: Add all the elements and divide it by the length of list.
●	To find median: sort the list in ascending order then return the middle value of the list.
●	To find mode: return the element occurring most number of times.
"""
class ct:
    def __init__(self, l=None):
        if l is None:
            l = []
        self.l=l

    def addValue(self,num):
        self.l.append(num)

    def removeValue(self,num):
        self.l.remove(num)

    def mean(self):
        sum=0
        for x in self.l:
            sum+=x
        return sum/len(self.l)

    def median(self):
        self.l.sort()
        median_index=len(self.l)//2
        return self.l[median_index]

    def mode(self):
        mode=None
        for x in range(len(self.l)-1):

            if self.l.count(self.l[x])>self.l.count(self.l[x+1]):
                mode = self.l[x]
        return mode

l=[1,2,3,4,5,6,6,6,7,8,7,8,9,9,4]
a=ct(l)
a.addValue(9)
a.removeValue(6)
print(a.l)
print(a.mean())
print(a.mode())
print(a.median())

"""
Rishi just learned about inheritance and now he is interested to know whether he can inherit the methods from the 
inbuild data structure of python or not. He wants to create his custom list with the name of class: advList -> ( Advance list ). 
There he wants to add few advance methods like getSecondMax() and getSecondMin(). 
Note: To get the second largest and second smallest number sort the list using bubble sort or 
selection sort the return the second last or second element respectively.
"""
class advList(list):
    def __init__(self,data):
        self.lst=data

    def getSecondMax(self):
        print(self.lst)
        one,two=1,2
        while self.lst[-one]==self.lst[-two]:
            one,two=one+1,two+1
        print(self.lst[-two])

    def getSecondMin(self):
        one,two=0,1
        while self.lst[one]==self.lst[two]:
            one,two=one+1,two+1
        print(self.lst[two])

list=[5,2,6,3,7,4,7,6,7,8,2]
aa=advList(list)
print(aa.lst)
aa.lst.sort()
print(aa.lst)
aa.getSecondMax()
aa.getSecondMin()
