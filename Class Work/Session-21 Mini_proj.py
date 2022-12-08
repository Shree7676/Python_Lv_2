"""
Chirag learned four different sorting algorithms. He wants to know the best sorting algorithm
( which takes minimum time to sort a given list ). To find out the answer he thought of the following steps:
Creating a list of 10,000 random numbers.
Sorting the same list with the help of four different algorithms
Calculating time taken to sort the list by each algorithm.
Repeating this process 1000 times and adding time_taken by different algorithms to get the significant time for comparison.
Providing rank on the basis of time_taken to sort the list by each algorithm.

Note: In different scenarios, different sorting algorithms are preferred. Find out all those situations as well.
"""
# bubble vs selection vs insertion vs Merge vs quick
import random
import time

def random_10000():
    List=[]
    for x in range(10000):
        List.append(random.randint(1,1000))
    return List

def selection_sort(l):

    for i in range(len(l)):
        min = i
        for j in range(i + 1, len(l)):
            if l[min] > l[j]:
                min = j
        l[i],l[min] = l[min],l[i]

def bubble_sort(l):

    for x in range(len(l)):
        for y in range(len(l)-x-1):
            if l[y]>l[y+1]:
                l[y],l[y+1]=l[y+1],l[y]

def insertion_sort(l):

    for x in range(1,len(l)):
        while l[x-1]>l[x] and x-1!=-1:
            l[x-1],l[x]=l[x],l[x-1]
            x-=1

def Merge_arr(l1,l2,l):
    i=j=k=0

    while i<len(l1) and j<len(l2):
        if l1[i]<=l2[j]:
            l[k]=l1[i]
            i+=1
        else:
            l[k]=l2[j]
            j+=1
        k+=1
    while i<len(l1):
            l[k]=l1[i]
            k+=1
            i+=1
    while j<len(l2):
            l[k]=l2[j]
            j+=1
            k+=1

def merge_sort(arr):
    if len(arr)<=1:
        return
    mid=len(arr)//2
    arr1=arr[:mid]
    arr2=arr[mid:]

    merge_sort(arr1)
    merge_sort(arr2)
    Merge_arr(arr1,arr2,arr)

def quicksort(arr, left, right):
    if left < right:                        # it stops bcz when we get divided=0 then right is -1 which is less then left
        divided = partition(arr, left, right)

        quicksort(arr, left, divided - 1)   # Recursion on left side
        quicksort(arr, divided + 1, right)  # Recursion on right side

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:                             # will run untill they meet eachother >> that is when 1 iteration is completed
        while i < right and arr[i] < pivot:  # it will stop when left side is greater then pivot
            i += 1
        while j > left and arr[j] >= pivot:  # it will stop when right side is less then or equal to pivot
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:                      # when they cross eachother
        arr[i], arr[right] = arr[right], arr[i]

    return i                                # divided position
ss=bs=iso=ms=qs=0
for x in range(1000):
    l=random_10000()

    start=time.time()
    selection_sort(l)
    end=time.time()
    ss+=end-start
    print("done ss")

    start=time.time()
    bubble_sort(l)
    end=time.time()
    bs+=end-start
    print("done bs")

    start=time.time()
    insertion_sort(l)
    end=time.time()
    iso+=end-start
    print("done is")

    start=time.time()
    merge_sort(l)
    end=time.time()
    ms+=end-start
    print("done ms")
    print(x)

"""    start=time.time()
    quicksort(l,0,len(l)-1)
    end=time.time()
    qs+=end-start"""

dic={"selection sort":ss,"bubble sort":bs,"insertion sort":iso,"merge sort":ms} #,"quick sort":qs}
for x in dic:
    print(f"Time taken by {x}",dic[x]/1000)

#got output after aprox 1 hr
"""
done ss
done bs
done is
done ms
999
Time taken by selection sort 2.9468077204227447
Time taken by bubble sort 3.0614468030929567
Time taken by insertion sort 0.0008406567573547363
Time taken by merge sort 0.021139708042144774

Process finished with exit code 0

"""