i=0 #WHILE LOOP
sum=0
numbercount=0
while i<=10:
    if i%2==0:
        print(i)
        sum+=i
        numbercount+=1
        
    i+=1
    

print(f"average value={sum/numbercount}") #f-string

for X in range(1,8,2): #FOR LOOP
    print(X)
print("descending order")
for X in range(5,0,-1):
      print (X)

#STRING
name="SNEHA"

print(name[2])
print(name[len(name)-1])

n=10
print("value"+str(n)) #to store integer in sting use str


name="SNEHA"
print(name[-1:-6:-1])
print(name[-1:-6:-2])
print(name[-1:-6:-3])
print(name[-1:-6:-4])


#LIST
listdata=[10,3.456,"SNEHA"]
print(listdata)
print(listdata[0])
for X in range(0,len(listdata)):
 print(listdata[X])

for X in listdata:
    print(X)

name="RAM"
for X in name:
    print(X)


#adding value to list at last
listdata.append(18)
print(listdata)

#insert using index u can add wherever you want
listdata.insert(1,45)
print(listdata)

#delete last value by default
listdata.pop()
print(listdata)

#delete by value
listdata.remove(10) 
print(listdata)

#delete specifically
listdata.pop(2)
print(listdata)

#delete overall list
listdata.clear()
print(listdata)

scores=[96,98,86,98]
print(max(scores)) #MAXIMUM
print(min(scores)) #MINIMUM


#Sort in asscending order
scores.sort()
print(scores)

#Sort in descending order
scores.sort(reverse=True)
print(scores)

#LIST COMPREHENSION
processedList=[v for v in scores if v>90]
print(processedList)
processedList=[float (v) for v in scores if v>90]

processedList=[v for v in scores if v%2==0]
print(processedList)

#TUPLE
tupledata=(10,20,30)
print(tupledata)
print(type(tupledata))

tupledata=(3.14,450)
print(tupledata)

tupledata =(3.14) #float
print(type(tupledata))
tupledata =(3.14,) #tuple
print(type(tupledata))
#USE concept of index to read value of tuple

#SETS  used to remove duplicate
setdata={10,20,30,40,40}
print(setdata)

#convet list to set
listofUSN=["R23EN154","R23EN158","R23EN154"]
setUSN=set(listofUSN)
listofUSN=list(setUSN)
print(listofUSN)

for i in listofUSN:#set doesn't have order /index
    print(i)

setUSN.remove("R23EN158")
print(setUSN)

setUSN.add("R783829")
print(setUSN)

set1={10,20,40,50}
set2={10,45,56,50}
print("Intersection=",set1.intersection(set2))
print("UNION=",set1.union(set2))
print("differece:",set1.difference(set2))
print("differece:",set2.difference(set1))

#Dictionaries
d={"name":"SNEHA","USN":"R23EN154","Branch":"ECE"}
print(type(d))
print(d)
d={"name":"SNEHA","name":"SNEHA","USN":"R23EN154","Branch":"ECE"}
print(d)
d={"name":"SNEHA","name":"Sahana","USN":"R23EN154","Branch":"ECE"}
print(d)

#read a vlues from dictionaries
print(f"name:{d['name']}")

#update
d["name"]='ram'
print(d)

#Adding new key
d["city"]="bengaluru"
print(d)

#remove
d.pop("city")
print(d)

ecommercedata=[
    
    {"product":"iphone","quantity":"123","price":"95000 each"},
    {"product":"ipad","quantity":"80","price":"65000 each"},
    {"product":"macbook","quantity":"20","price":"85000 each"}
]
