N=int(input())

for i in range(N):
    for j in range(N):
        print(f"({N-i},{N-j})",end=" ")
    print()