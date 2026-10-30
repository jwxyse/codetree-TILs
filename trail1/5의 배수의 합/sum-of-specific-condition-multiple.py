arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]

if A<B:
    A_sum=0
    while A<=B:
        if A%5==0:
            A_sum+=A
        A+=1
    print(A_sum)

elif A>B:
    B_sum=0
    while A>=B:
        if B%5==0:
            B_sum+=B
        B+=1
    print(B_sum)

else:
    if A%5==0:
        print(A)
    else:
        print(0)