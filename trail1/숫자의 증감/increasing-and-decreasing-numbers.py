arr=input().split()

C=arr[0]
N=int(arr[1])

if C=='A':
   i=1
   while i<=N:
        print(i,end=" ")
        i+=1
elif C=='D':
   i=N
   while i>=1:
        print(i,end=" ")
        i-=1
