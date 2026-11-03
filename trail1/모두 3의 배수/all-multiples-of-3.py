satisfied=True

for i in range(1,6):
    N=int(input())
    if N%3!=0:
        satisfied=False
        break

if satisfied==True:
    print(1)
else:
    print(0)