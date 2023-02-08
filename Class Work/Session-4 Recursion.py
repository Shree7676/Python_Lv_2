
#Create a function printDecreasing(n) that can print all the number from n to 1 in decreasing order using recursion.

def printDecreasing(n):
    
    # Base case
    if n == 0 :
        return 
    
    print(n) # print n on screen
    
    printDecreasing(n-1) 
    
print("To print all the numbers from n to 1 in decreasing order.")
n = int(input("Enter the number n :"))

printDecreasing(n)




#Create a function printIncreasing(n) that can print all the numbers from 1 to n in increasing order using recursion.

def printIncreasing(n):
    
    # Base case
    if n == 0 :
        return 
    
    printIncreasing(n-1) 
    
    print(n) # print n on screen
    
print("To print all the numbers from 1 to n in increasing order.")
n = int(input("Enter the number n :"))

printIncreasing(n)




"""
The factorial of a number is the product of all the integers from 1 to that number. Chris thought to find the factorial of number 20 manually. He had no idea how big factorial of 20 is. After multiplying numbers up to some extent, his calculator started using the e ( exponent of 10 ) format for the answer. Write a program in python to find the factorial of a number using recursion and tell your friends how big that number is.
"""
def factorial(number):
    
    if number == 0 :
        return 1
    
    return number * factorial(number-1)


num = int(input("Enter a number to find factorial :"))

print(factorial(num))





"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 
Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.
Image illustration for 3 disks :

Chirag observed that the same steps are repeated again and again in the Tower of Hanoi problem. He thought this problem can be solved with the help of recursion in python. His friend Chris said it is impossible. Write a program in python and create a function to solve the Tower of Hanoi problem. Also, share your program with your programmer friends.
The output of the program should look like this:
If there are only two disks:
Input: 2
Output: Disk 1 moved from A to B
        Disk 2 moved from A to C
        Disk 1 moved from B to C

If there are three disks:
Input: 3
Output: Disk 1 moved from A to C
        Disk 2 moved from A to B
        Disk 1 moved from C to B
        Disk 3 moved from A to C
        Disk 1 moved from B to A
        Disk 2 moved from B to C
        Disk 1 moved from A to C
"""         
def towerOfHanoi(n , from_rod , to_rod , help_rod):
    
    if n == 0 :
        return 
    
    towerOfHanoi(n-1 , from_rod, help_rod , to_rod)
    print("Move disk " , n , "from " , from_rod , " to " , to_rod)
    towerOfHanoi(n-1 , help_rod , to_rod , from_rod)
    
    
n = int(input("Enter the number of disk to move from rod A to rod B with the help of rod C : "))

towerOfHanoi(n , "A" , "C" , "B")



