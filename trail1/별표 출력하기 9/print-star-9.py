N=int(input())

for i in range(N):
    for j in range((N-1)-(1*i)):
        print(" ",end=" ")
    
    for j in range(2*i+1):
        print("*",end=" ")
    print()