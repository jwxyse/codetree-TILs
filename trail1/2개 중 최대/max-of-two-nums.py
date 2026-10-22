arr=list(map(int,input().split()))

A=arr[0]
B=arr[1]

a=arr[0] if arr[0]>arr[1] else arr[1]
print(a)