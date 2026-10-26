arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]
C=arr[2]

if A<B:
    if B<C:
        print(B)
    elif B>C:
        if A<C:
           print(C)
        else:
            print(A)

if A>B:
    if A<C:
        print(A)
    elif A>C:
        if C>B:
            print(C)
        else:
            print(B)
        


