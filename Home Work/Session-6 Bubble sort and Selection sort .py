"""
Homework questions

Arunima is aware of the inbuilt sorted() function. She is very interested to know how we can create our manual sorting function. To show the same thing to Arunima write a python program and create sortIt() function. Use any suitable sorting algorithm inside this function and return the sorted list.
"""
def sortIt(lst):
    for i in range(len(lst)):
        smallest = 1 
        for j in range(i+1,len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]
    return lst



sampleList = [1,3,5,7,9,0,2,4,6,8,10]
sort = sortIt(sampleList)
print(sort)

"""
Chirag learned two new sorting algorithms, bubble sort, and selection sort. For him, bubble sort is easy as compared to selection sort. But still, he wants to know which of these two sorting algorithms is more efficient. He wants to compare the number of comparisons and the number of swaps made in sorting a list. Write a program to do the same thing and find which of these sorting algorithms is efficient.
"""
sampleList = [10,9,8,7,6,5,4,3,2,1]


#bubble sort

sampleList = [10,9,8,7,6,5,4,3,2,1]
bubbleCounter = 0
for i in range(len(sampleList)-1):
    for j in range(len(sampleList)-i-1):
        if sampleList[j] > sampleList[j+1]:
            sampleList[j], sampleList[j+1] = sampleList[j+1], sampleList[j]
            bubbleCounter += 1

#selection sort
sampleList = [10,9,8,7,6,5,4,3,2,1]
selectionCounter = 0
for i in range(len(sampleList)):
    smallest = i
    for j in range(len(sampleList)-1):
        if sampleList[smallest] > sampleList[j]:
            smallest = j
    sampleList[i] , sampleList[smallest] = sampleList[smallest], sampleList[i]
    selectionCounter +=1



print(bubbleCounter)
print(selectionCounter)




"""
Conceptual Question required to understand selection sort :

Find out the smallest value of a list without making any change in the list. 
Hint: User for loop and make the comparisons.
"""
sampleList = [9,11,18,2,14,999,5,79,69,420]
smallestValue = sampleList[0]
for i in range(len(sampleList)):
    if smallestValue > sampleList[i]:
        smallestValue = sampleList[i]

print(smallestValue)


