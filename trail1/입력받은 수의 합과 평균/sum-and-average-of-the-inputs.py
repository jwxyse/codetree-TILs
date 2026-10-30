N=int(input())
sum_val=0
cnt=0

for i in range(1,N+1,1):
    a=int(input())
    sum_val+=a
    cnt+=1

print(sum_val,f"{sum_val/cnt:.1f}")