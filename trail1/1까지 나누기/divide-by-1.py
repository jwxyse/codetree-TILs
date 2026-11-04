N=int(input())

cnt=0
div=1

while N>1:
    if N>1:
        N=N//div
        cnt+=1
        div+=1

    else:
        break

print(cnt)