arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]

if A>B: 
    while A>=B:
        print(A,end=" ")
        A-=1
elif A<B:
    while A<=B:
        print(B,end=" ")
        B-=1
else:
    print(A)
