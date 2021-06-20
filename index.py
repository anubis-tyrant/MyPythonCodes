str=input("enter your things: ")
l=len(str)
list=[]
for i in range(0,l):
    if str[i].isupper():
        
        list.append(i)

print("the indices of all caps is",list)
