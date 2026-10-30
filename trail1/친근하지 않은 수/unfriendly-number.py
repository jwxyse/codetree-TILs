N=int(input())

cnt=0
i=1

while i<=N:
    if i%2==0 or i%3==0 or i%5==0:
        pass
    else:
        cnt+=1
    i+=1

print(cnt) 