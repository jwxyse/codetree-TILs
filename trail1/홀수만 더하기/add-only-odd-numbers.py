N=int(input())
i=1
sum_val=0


while i <= N:
    a=int(input())
    if a%3==0 and a%2==1:
        sum_val+=a

    i+=1

print(sum_val)