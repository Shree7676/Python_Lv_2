import numpy as np
import pandas
"""
a= np.array([[[1,2,3,4],[1,2,3,4]]])
print(a)
print(np.ndim(a)) 


b=np.array([5,6,7,8],ndmin=5)
print(b)
print(np.ndim(b)) 

#array 0
a0=np.zeros(4)
print(a0)
print(np.ndim(a0))
a0_2=np.zeros((3,4,2))
print(a0_2)
print(np.ndim(a0_2))


a1=np.ones(3)
print(a1)

empty=np.empty(4)
print(empty)


# range array

ra=np.arange(4,10,2)
print(ra)


#diagonal is 1
d=np.eye(3)
print(d)

#linespace >> [ 0.   2.5  5.   7.5 10. ]
l=np.linspace(0,10,num=5)
print(l)


#fnc >> rand >> randn 
#randn gives +ve and -ve number also
#randint(min,max,total number)

r=np.random.rand(5)
print(r)

r_multi=np.random.rand(2,5,3)
print(np.ndim(r_multi))
print(r_multi)



#Arthmetic operators
#1D
x=np.array([1,2,3,4])
print(x+6)  # - / * ** 
y=np.ones(4)
print(x+y)

#2D
x2=np.array([[1,7,3,9],[5,6,7,8]])
y2=np.array([[1,1,1,1],[1,1,1,1]])

print(x2+y2)

#Arthmetic fnc
print(np.min(x))
print(np.min(x2,axis=0),"2 d array ka min")
print(np.min(x2,axis=1),"2 d array ka min")
print(np.max(x))
print(np.sqrt(x))
print(np.argmax(x)) #gives index of max number
print(np.argmin(x)) #gives index of min number

#numpy shape reshape
"""
a=np.arange(1,10,2)
a=np.array(a,ndmin=5)