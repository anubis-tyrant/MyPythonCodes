def fact(x):
	c=1
	if x==1:
		return x
	else:
		for i in reversed(range(1,x+1)):
			if i!=1:
				c=c*i
		print(c)

num=int(input("Enter number to find factorial of: "))
fact(num)