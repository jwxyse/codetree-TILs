arr=list(map(int,input().split()))

a=arr[0]
b=arr[1]

for i in range(a,b+2):
    if i%2==1:
        print(i,end=" ")