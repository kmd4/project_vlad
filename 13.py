def f(s, e, k=[]):
    if s == e: return 1
    if s == 12 or s > e: return 0
    if s > 8 and 8 not in k: return 0
    return f(s + 1, e, k=k+[s + 1]) + f(s * 4, e, k = k + [s * 4])
print(f(2, 90))


