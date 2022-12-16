"""
Homework questions

Chris said we can sort the list only in ascending order using the insertion sort algorithm. Chirag thinks we can even sort the list in descending order. To help Chirag and to show Chris write a program to sort a list of numbers in descending order using the insertion sort algorithm.
"""
def sortit(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j>=0 and key>lst[j]:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = key
    return lst



sampleList = [5,6,7,8,9,1,2,3,0]
sortedList = sortit(sampleList)
print(sortedList)



"""
Himanshi knows about binary search but she is not aware that the list should be sorted before you apply the binary search algorithm. Due to this misconception, she was getting errors. So sort the list and then apply the binary search algorithm to find any item in the list.
Note: Use insertion sort algorithm
"""
def sortit(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key<lst[j]:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = key 
    return lst

sampleList = [8,4,2,1,6,7,3,0,5,9]
sortedList = sortit(sampleList)
print(sortedList)

element = int(input("What number are yo looking for?"))
low = 0 
high = len(sortedList)-1
mid = (low+high)//2
while low <= high:
    if element == sortedList[mid]:
        print(mid)
        break
    elif element < sortedList[mid]:
        high = mid - 1
        mid = (low+high)//2
    else:
        low = mid + 1
        mid = (low+high)//2
print("End")




