"""
Homework questions 

Chris wants to know how a binary search algorithm is better than a linear search algorithm. To compare these two algorithms he created a sorted list of 10000 numbers and a random number between 1 to 10000. He checked how many comparisons are made to find the number in both the algorithms. For a better result, he repeated this entire process 100 times. At the end, he compared the number of comparisons in both algorithms. Do the same thing and find the given ratio:
Number of comparisons in linear search: Number of comparisons in binary search
Hint: 
Use for-loop to create the sorted list of first 10,000 numbers
Use randint() function to generate a random number between 1 to 10,000
"""
from random import randint


def linearSearchComparision(lst , number):
    comparisions = 0 
    
    for i in lst :
        if i == number :
            return comparisions 
        
        comparisions += 1 
        
def binarySearchComparision(lst , number):
    comparisions = 0 
    
    low = 0 
    high = len(lst)-1
    mid = (low+high) //2
    
    while ( low <= high ) :
        
        mid = (low+high) //2
        
        if lst[mid] == number :
            return comparisions 
        
        elif lst[mid] > number :
            high = mid - 1
            comparisions += 1
            
        else :
            low = mid + 1
            comparisions += 1
        
    else :
        return None 
    

lst = []

for i in range( 1, 10001):
    lst.append(i)
    
linearComparisions = [] 
binaryComparisions = []

for i in range(100) :
    number = randint(1 , 10000)
    
    linearComparision = linearSearchComparision(lst , number)
    linearComparisions.append(linearComparision)
    
    binaryComparision = binarySearchComparision(lst , number)
    binaryComparisions.append(binaryComparision)
totalLinear = sum(linearComparisions)
totalBinary = sum(binaryComparisions)

print(totalLinear)
print(totalBinary)

print("Linear to Binary Ratio :")
print(totalLinear/totalBinary)
"""
In a class, the roll number of the students are assigned in alphabetical order. The class monitor requires the roll number of the students. To make his work easier he decided to write a program in python to store all the names in a list. He wanted to apply a linear search algorithm to find out the roll number of any student. Write a program according to the given condition. ( Create a function that takes the name as a parameter and return the roll number of the given name )
Note: The roll number of the student is equal to index+1 in the given list.
Hint: 
Create a sample list of 10 students' name 
Sort it using the sort() method 
Apply linear search algorithm on the sorted list.
Print the roll number ( index + 1 ) on the screen
"""
studentList = ["Moksha", "Vishesh", "Pranav", "Naimisha", "Radha," "Palavi", "Rashmika", "Mahendra", "Candy","Jaimin"]
studentList.sort()

def getRollNumber(name):
    for i in range(len(studentList)):
        if name == studentList[i]:
            return i+1
    return "Student not found"

studentName = input("Enter the name of the student you are searching for:")

rollNumber = getRollNumber(studentName)
print(rollNumber)









Binary Search Algorithm code:

lst = [2,3,54,64,76,78,81,88,91]

element = int(input("Enter the number to search :"))

low = 0 
high = len(lst)-1

flag = 0

while ( high >= low ):
    
    mid = (high+low)//2
    
    if element == lst[mid] :
        print(mid)
        flag = 1
        break

    elif element > lst[mid] :
        low = mid + 1
        
    else :
        high = mid - 1
        
    mid = (high+low)//2
        
if flag == 0 :
    print("The element is not present in the list.")


