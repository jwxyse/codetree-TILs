arr=list(map(int,input().split()))

h=arr[0]
w=arr[1]

b=int(w/((h/100)**2))
print(b)

if b>25:
    print("Obesity")