arr=list(map(int,input().split()))

print(sum(arr))
print(int(sum(arr)/len(arr)))
print(int(sum(arr)-(sum(arr)/len(arr))))