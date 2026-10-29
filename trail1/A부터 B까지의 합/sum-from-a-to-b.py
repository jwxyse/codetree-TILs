arr=list(map(int,input().split()))

a=arr[0]
b=arr[1]

sum_val=0

while a<=b:
    sum_val+=a
    a+=1

print(sum_val)