arr_A=list(map(int,input().split()))
arr_B=list(map(int,input().split()))

A_Math=arr_A[0]
A_English=arr_A[1]

B_Math=arr_B[0]
B_English=arr_B[1]

if A_Math>B_Math:
    print("A")
elif A_Math==B_Math:
    if A_English>B_English:
        print("A")
    else:
        print("B")
else:
    print("B")

