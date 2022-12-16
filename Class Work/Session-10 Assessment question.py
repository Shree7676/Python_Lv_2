
"""
After a surprise class test, the teacher wants two different lists of students.
One of them should be sorted according to the names of the student and the second one
should be sorted according to the marks they obtained.

Hint:
Create a dictionary with the name of students as key and their marks as value. Then print the sorted key and values.
Example:
students = { "Arvind":98 , "Nidhi":100 , "Kunal":99 }
Name of students in alphabetical order:
Arvind
Kunal
Nidhi
Name of students according to their marks:
Nidhi
Kunal
Arvind
Note: Take the input from the user to fill the dictionary and use bubble or selection sort for sorting.
"""
students = { "ram":101 , "sham":100 , "kaam":99 }

def Bsort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                lst[j+1],lst[j]=lst[j],lst[j+1]

sort_names=[]
marks_sort=[]
marks_sort_name=[]

def sort_name(students):
    for x in students.keys():
        sort_names.append(x)
    Bsort(sort_names)

def sort_name_marks(students):
    for x in students.values():
        marks_sort.append(x)
    
    Bsort(marks_sort)
    marks_sort.reverse()   #or run the loop in reverse order
    for x in marks_sort:
        for k,v in students.items():
            if v==x:
                marks_sort_name.append(k)

sort_name(students)
sort_name_marks(students)
print(sort_names)
print(marks_sort_name)

#que2
"""
Abhishek and his friends decided to play cricket. They were not able to divide themself into two groups perfectly. 
Abhishek thought that the team should be divided randomly into two parts. 
Write a program in python to help them in dividing the group randomly into two parts.

Note: 
Create a shuffle function to shuffle the elements of the list then divide it into two parts.
Hint: 
Use sorting algorithm, random module, and recursion.
Create a list by taking the input from the users and then print two lists on the screen with team A and team B.
Example:
Enter the name of the player: Shubham 
Repeat around 22 times to take input
Players = ["Shubham","Arvind",....]
teamA = ["Shubham"....]
teamB = ["Arvind"....]
"""
#que doesnt make sense if we include sorting algo... 
#so doing it normally please let me know why sorting will be used here if u have any idea

import random

arr=["Shubham","Arvind","ram","rahul","karan","arjun","nakul","bheem"]
teamA = []
teamB = []
def shuffle(arr):
    if arr==[]:
        return

    if len(arr)==1:
        r=random.randint(1,2)
        if r==1:
            teamA.append(random.choice(arr))
            arr.remove(teamA[-1])
            return
        else:
            teamB.append(random.choice(arr))
            arr.remove(teamB[-1])
            return

    
    teamA.append(random.choice(arr))
    arr.remove(teamA[-1])           # the latest item that was added

    teamB.append(random.choice(arr))
    arr.remove(teamB[-1])
    shuffle(arr)

print(shuffle(arr))
print(teamA)
print(teamB)




