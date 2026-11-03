N=int(input())
satisfied=False

for i in range(2,N):
    if N%i==0:
        satisfied=True

if satisfied==True:
    print("C")
else:
    print("P")