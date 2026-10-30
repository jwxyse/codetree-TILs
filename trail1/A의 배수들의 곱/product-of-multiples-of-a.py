arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]
prod=1
if A<=B: 
    for i in range(1,B+1):
        if i%A==0:
            prod*=i

elif A>=B:
    for i in range(1,A+1):
        if i%B==0:
            prod*=i

print(prod)