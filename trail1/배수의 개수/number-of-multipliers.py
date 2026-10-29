i=1
cnt_3=0
cnt_5=0

while i<=10:
    n=int(input())
    i+=1
    if n%3==0 :
        cnt_3+=1

    if n%5==0:
        cnt_5+=1

print(cnt_3,cnt_5)