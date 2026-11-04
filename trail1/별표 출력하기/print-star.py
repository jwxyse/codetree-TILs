N=int(input())
cnt=1

for i in range(2*N-1):
    for j in range(cnt):
        print("*",end=" ")
    print()

    if i>N-2:
        cnt-=1

    else:
        cnt+=1