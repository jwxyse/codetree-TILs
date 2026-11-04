N=int(input())

for i in range(N-1):
    for j in range(i+1):
        print("*",end="")
    print()
    print()

for i in range(N):
    for j in range(N-i):
        print("*",end="")
    print()
    print()
    
