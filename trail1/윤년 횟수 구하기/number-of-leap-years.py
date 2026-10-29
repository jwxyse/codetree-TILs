N=int(input())
cnt=0
i=1

while i<=N:
    if i%100==0 and i%400!=0:
        pass
    elif i%4==0:
        cnt+=1

    i+=1

print(cnt)