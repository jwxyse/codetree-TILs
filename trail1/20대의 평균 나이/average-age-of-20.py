sum_age = 0
cnt = 0

while True:
    age = int(input())

    if age < 20 or age >= 30:
        break

    sum_age += age
    cnt += 1

print(f"{sum_age / cnt:.2f}")