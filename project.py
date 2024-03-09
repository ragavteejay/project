n=int(input("enter the number"))
for i in range(n,0,-1):
    print("*"*i,end="")
    print(" "*((n-i)*2),end="")
    print("*"*i)
for i in range(2,n+1,1):
    print("*"*i,end="")
    print(" "*((n-i)*2),end="")
    print("*"*i)