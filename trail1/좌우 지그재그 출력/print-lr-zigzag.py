N = int(input())

for i in range(N):
    if i % 2 == 0:
        for j in range(1, N + 1):
            print(i * N + j, end=" ")
    else:
        for j in range(N, 0, -1):
            print(i * N + j, end=" ")

    print()