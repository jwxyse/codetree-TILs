arr=list(map(int,input().split()))

a=arr[1]
b=arr[0]

for i in range(b,a-1,-1):
    if i%2==1:
        print(i,end=" ")