arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]
prod=1

for i in range(A,B+1,1):
    prod*=i


print(prod)