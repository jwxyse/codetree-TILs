arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]

if A>0:
    for i in range(B):
        print(A,end="")
        i+=1

else:
    print(0)