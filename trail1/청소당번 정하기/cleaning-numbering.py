n=int(input())
cnt_2=0
cnt_3=0
cnt_12=0
i=1

while i<=n:

    if i%12==0:
        cnt_12+=1
    elif i%3==0:
        cnt_3+=1
    elif i%2==0:
        cnt_2+=1

    i+=1

print(cnt_2,cnt_3,cnt_12)