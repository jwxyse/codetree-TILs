arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]

while A<=B:
    if A%2==0:
        print(A,end=" ")
    A+=1