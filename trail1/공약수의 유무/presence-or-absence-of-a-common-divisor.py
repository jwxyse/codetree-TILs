arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]
satisfied=False

for i in range(A,B+1):
    if 1920%i==0 and 2880%i==0:
        satisfied=True

if satisfied==True:
    print(1)
else:
    print(0)
