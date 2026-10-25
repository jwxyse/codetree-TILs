arr=list(map(int,input().split()))

M=arr[0]
L=arr[1]

if M >= 90:
    if L >= 95:
        print("100000")
    elif L <90:
        print("0")
    else:
        print("50000")
else:
    print("0")