arr=list(map(int,input().split()))

a=arr[0]
b=arr[1]
c=arr[2]

satisfied=False

for i in range(a,b+1):
    if i%c==0:
        satisfied=True

if satisfied==True:
        print("YES")
else:
        print("NO")