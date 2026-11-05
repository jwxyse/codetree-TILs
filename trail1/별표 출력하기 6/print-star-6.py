N = int(input())

# 위쪽 + 가운데
for i in range(N):
    for j in range(i):
        print("  ", end="")

    for j in range(2 * N - 1 - 2 * i):
        print("* ", end="")

    print()

# 가운데 아래쪽
for i in range(N - 2, -1, -1):
    for j in range(i):
        print("  ", end="")

    for j in range(2 * N - 1 - 2 * i):
        print("* ", end="")

    print()