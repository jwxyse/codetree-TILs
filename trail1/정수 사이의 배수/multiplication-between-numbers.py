arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]

sum_val=0
cnt=0

while A<=B:
    if A%5==0 or A%7==0:
        sum_val+=A
        cnt+=1
    A+=1

print(sum_val,f"{sum_val/cnt:.1f}")