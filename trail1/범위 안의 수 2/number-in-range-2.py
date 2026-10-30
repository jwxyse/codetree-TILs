sum_val=0
cnt=0
i=1

while i<=10:
    n=int(input())
    if 0<=n<=200:
        sum_val+=n
        cnt+=1
    
    i+=1

print(sum_val,f"{sum_val/cnt:.1f}")