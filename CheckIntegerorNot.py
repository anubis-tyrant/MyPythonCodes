def Checkint(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


lst=[22,"hi",4,"eee",33,4221,5,3,5,"haha",2,"2223"]
lst2=[]
for i in lst:
#    print(i)
    if Checkint(i)==False:
        lst2.append(i)
print(lst2)
