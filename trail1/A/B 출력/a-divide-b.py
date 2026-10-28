arr=list(map(int,input().split()))

a=arr[0]
b=arr[1]

print(a//b,end=".")
rest=a%b

for i in range(20):
    rest=rest*10
    print(rest//b,end="")
    rest=rest%b