arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]

print(A,end=" ")

while A<=B:
    if A%2==0:
        A=A+3
        if A<=B:
            print(A,end=" ")
        else:
            pass
    elif A%2==1:
        A=A*2
        if A<=B:
            print(A,end=" ")
        else:
            pass