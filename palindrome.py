str=input("Enter nam: ")
str2=""
for i in reversed(range(len(str))):
		str2=str2+str[i]
#str2=str[::-1]		
if str2==str:
	print("True")
else:
	print ("False".)

#reverse(str)