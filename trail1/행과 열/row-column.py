arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]

for i in range(1,A+1):
    for j in range(1,B+1):
        print(i*j,end=" ")
    print()