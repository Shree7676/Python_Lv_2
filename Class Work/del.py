arr=[7,6,4,3]

for x in range(len(arr)-1):
    for y in range((len(arr)-1)-x):
        if arr[y]>arr[y+1]:
            arr[y],arr[y+1]=arr[y+1],arr[y]

print(arr)