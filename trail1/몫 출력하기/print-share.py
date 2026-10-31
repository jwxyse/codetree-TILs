sum2 = 0

while True:
    a = int(input())

    if a % 2 == 1:
        continue

    if a % 2 == 0:
        print(a // 2)
        sum2 += 1

        if sum2 == 3:
            break