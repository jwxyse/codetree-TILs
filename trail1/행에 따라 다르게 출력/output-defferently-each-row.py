N = int(input())

num = 0

for i in range(N):
    if i % 2 == 0:       # 1, 3, 5...번째 줄
        for j in range(N):
            num += 1
            print(num, end=" ")
    else:                # 2, 4, 6...번째 줄
        for j in range(N):
            num += 2
            print(num, end=" ")

    print()