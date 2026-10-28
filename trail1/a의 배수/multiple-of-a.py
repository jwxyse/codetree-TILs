arr=list(map(int,input().split()))

N=arr[0]
a=arr[1]

i=1

while i<=N:
    if i%a==0:
        print(1)
    else:
        print(0)
    i+=1