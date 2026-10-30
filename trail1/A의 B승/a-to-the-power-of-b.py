arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]
prod=1
i=1

while i<=B:
    prod*=A
    i+=1

print(prod)