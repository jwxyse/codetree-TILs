arr=list(map(int,input().split()))

a=arr[0]
b=arr[1]

if a>b:
    print(a*b)
else:
    print(b//a)