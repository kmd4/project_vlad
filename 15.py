with open('14.txt') as f:
    k = 0
    maxx = 100000
    a = f.read().split('\n')[:-1]
    a = list(map(lambda x: int(x),a))
    for i in range(len(a)):
        print(i)
        if a[i] % 7 == 0 and a[i+1] % 7 ==0:
            k += 1
            maxx = min(maxx, a[i] + a[i+1])
print(k ,maxx)