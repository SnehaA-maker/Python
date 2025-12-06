name=input("enter a name  ")
for i in range(len(name)):
    if i%2==0:
        print(chr(ord(name[i])+1),end="")
else:
    print(name[i],end="")
