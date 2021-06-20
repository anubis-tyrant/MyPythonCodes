print("Hello Bish")
def dist(x1,y1,x2,y2):
    n1=abs(x1-x2)
    n2=abs(y1-y2)
    result=n1+n2
    print(result)
x1=int(input("Enter the X point of your 1st coord:"))
y1=int(input("Enter Y point now: "))
x2=int(input("Enter the Xpoint of the second coord: "))
y2=int(input("Enter Y now: "))

dist(x1,y1,x2,y2)

