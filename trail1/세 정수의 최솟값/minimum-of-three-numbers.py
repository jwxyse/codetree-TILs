arr=list(map(int,input().split()))
a=arr[0]
b=arr[1]
c=arr[2]

if a<b:
    min=a
else:
    min=b
if min<c:
    pass
else:
    min=c

print(min)