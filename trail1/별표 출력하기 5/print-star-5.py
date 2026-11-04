N=int(input())

for i in range(N):
    for j in range(N,i,-1):
        print("*"*(N-i),end=" ")
    print()