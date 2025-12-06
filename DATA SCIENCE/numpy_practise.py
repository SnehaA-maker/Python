import numpy as np
print(np.__version__)

#0D
arr=np.array([20])
print(arr)

#1D
arr=np.array([20,30,40])
print(arr)

#2D
arr=np.array([
    [1,2,3],
    [4,5,6]
])
print(arr)
print(f"No of dimension {arr.ndim}")

#3D
arr=np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [5,6,7],
        [8,5,6]
        ]
    ]
)
print(arr)
print(f"No of dimension {arr.ndim}")

arr=np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [5,6,7],
        [8,5,6]
        ]
    
])
print(arr.shape)
print(arr.size)

arr=np.array([10,20,30,40])
print("last value from array :",arr[arr.size-1])
print("first value from array :",arr[0])

arr=np.array([
    [10,20,30,40],
    [50,60,70,80]
])
print("2D array ",arr[1,3])

for d in arr:
    print(d) 

for d in arr: #d is a variable which stores array elements
    for sd in d: #sd is a variable which stores d elements
        print(sd)


print(type(arr))
arr=np.array([10,20,30,40])
print(arr.dtype)

arr=np.array([10,2.3345,30,40])
print(arr.dtype)

arr=np.array(["s","w","e"])
print(arr.dtype)

arr=np.array([10,20,30,40],dtype="S") #conversion of integer into string
print(arr.dtype)
print(arr)

array=np.array(["10","20","30"])
print(arr.dtype)

arr=np.array(["10","20","30"],dtype="i") #conversion of string into int
print(arr.dtype)

arr=np.array(["a","20","30"]) #checking type of mixed datatype
print(arr.dtype)

#arr=np.array(["a","20","30"],dtype="i") conversion of char into int is impossible 
#print(arr.dtype)

#operations of list are searching,sorting,filtering....

arr=np.array([88.2,34,67,89.3,45.4]) #to print index
x=np.where(arr==34)  #where is a function
print(x)

x=np.where(arr>=60)
print(x)

x=np.where(arr>=60)
for d in x:
    print(x)

z=arr[arr>=60] #to print value
for d in z:
    print(z)
 
y=np.where((arr>=60) & (arr<=90))
print(y)

 
arr=np.array((2,67,98,45,89))
x=np.sort(arr)
print(x)
y=np.flip(x)
print(y)
