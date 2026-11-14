N = int(input())

for i in range(N):
    for j in range(N):
        print((i * N + j) % 9 + 1, end="")
    print()