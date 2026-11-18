N = int(input())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j % 2 == 1:
            print(i, end="")
        else:
            print(N - i + 1, end="")
    print()