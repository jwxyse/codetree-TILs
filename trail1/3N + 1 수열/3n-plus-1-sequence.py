N=int(input())
sum_val=0

while True:
    if N==1:
        print(sum_val)
        break
    if N%2==0:
        N=N//2
        sum_val+=1
        continue
    if N%2==1:
        N=N*3+1
        sum_val+=1
        continue

