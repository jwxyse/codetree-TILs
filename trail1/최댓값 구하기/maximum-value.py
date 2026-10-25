arr=list(map(int,input().split()))

a=arr[0]
b=arr[1]
c=arr[2]

if a>=b:
    max=a
    if max>=c:
        print(max)
    else:
        print(c)
elif a<=b:
    max=b
    if max>=c:
        print(max)
    else:
        print(c)