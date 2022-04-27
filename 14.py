for x in range(1, 100):
    x1 = x
    L = 0

    M = 0

    while x > 0:

        L = L + 1

        if x % 8 < 5:
            M = M + (x % 8)

        x = x // 8

    if L == 2 and M == 1:
        print(x1)
        break
print(2 * 1024 / 64)
print(126/18)