arr=list(map(int,input().split()))

B=arr[0]
A=arr[1]

while B>=A:
    if B%2==0:
        print(B,end=" ")
    B-=1