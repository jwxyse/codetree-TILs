A=int(input())

for i in range(1,A+1):
    if (i//8)%2!=0 and not (i%2==0 and i%4!=0) and not i%7<4:
        print(i,end=" ")
        continue