N = int(input())

cnt = 2

for i in range(N):
    for j in range(N):
        print(cnt, end=" ")

        cnt += 2

        if cnt == 10:
            cnt = 2

    print()