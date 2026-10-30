arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]

sum_val=0

for i in range(A,B+1):
    if A%6==0 and A%8!=0:
        sum_val+=A
    A+=1

print(sum_val)
