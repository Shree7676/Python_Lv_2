# What is the mean of the first 10 natural numbers?
def mean(arr):
    sum=0
    for x in arr: sum+=x
    return sum/len(arr)

arr=[]
for x in range(1,11):
    arr.append(x)
print("mean=",mean(arr))


# Find the median of the following:
# 4, 17, 77, 25, 22, 23, 92, 82, 40, 24, 14, 12, 67, 23, 29
def median(arr):
    arr.sort()
    if len(arr)%2!=0:
        mid=round(len(arr)/2)
        return arr[mid-1]  #index position starts with zero so -1
    else:
        mid=round(len(arr)/2)
        return (arr[mid-1]+arr[mid])/2 #index position starts with zero so -1

print("median=",median([1, 3, 5, 7, 9, 11]))

# Find the mode of the given data set: 3, 3, 6, 9, 15, 15, 15, 27, 27, 37, 48.

def mode(arr):
    frequency=0
    ans=int()
    for x in arr:
        if arr.count(x)>frequency:
            frequency=arr.count(x)
            ans=x
    return ans

print("mode=",mode([3, 3, 6, 9, 15, 15, 15, 27,27, 37, 48]))


# Calculate the standard deviation for the following data:
data={
    "00-10":27,
    "10-20":10,
    "20-30":7,
    "30-40":5,
    "40-50":4,
    "50-60":2,
}

def sample_variance(arr):
    X=mean(arr)
    sum=0
    for xi in arr:
        sum+=(xi-X)**2
    return sum/(len(arr)-1)

def variance(arr):
    X=mean(arr)
    sum=0
    for xi in arr:
        sum+=(xi-X)**2
    return sum/len(arr)

def sample_std_div(arr):
    return (sample_variance(arr))**0.5
    
def std_div(arr):
    return (variance(arr))**0.5

print("sample_std_div=",sample_std_div([30,12,25,20,23]))
print("sample_variance=",sample_variance([30,12,25,20,23]))

# Determine the interquartile range value for the first ten prime numbers
#interquartile = thirdquartile - firstquartile

def quartile(arr,quart):
    arr.sort()
    n=len(arr) # in actual formula n=len(arr)+1   ...it always come in points so we just do int(). it will work 
    return arr[int(n*(quart/100))]

def interquartile(arr):
    return quartile(arr,75)-quartile(arr,25) # the diference between third quartile and first quartile is known as interquartile

def prime_num(num):
    for x in range(2,num):
        if num%x==0:
            return False
    return True
list=[]
num=2
while len(list)<10:
    if prime_num(num):
        list.append(num)
    num+=1

print("interquartile=",interquartile(list))
# 65, 41, 48, 12, 58, 2, 53, 47, 66, 25, 54 >> 33
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 >> 14
# 8,10,12,13,15,17,17,18,19,23 >> 6
