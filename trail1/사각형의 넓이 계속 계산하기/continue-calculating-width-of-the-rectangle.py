while True:
    width, height, c = input().split()

    width = int(width)
    height = int(height)

    print(width * height)

    if c == 'C':
        break