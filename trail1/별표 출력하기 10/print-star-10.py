N=int(input())
hall=1
zap=N

for i in range(N*2):
    if i%2==0:
        for j in range(hall):
            print("*",end=" ")
        print()
        hall+=1

    else:
        for j in range(zap):
            print("*",end=" ")
        print()
        zap-=1