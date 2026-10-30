arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]

sum_val=0

while A<=B:
    if A%2==0:
        sum_val+=A
    A+=1

print(sum_val)