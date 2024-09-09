def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    max_len = max(len(str(x)), len(str(y)))
    m = max_len // 2
    x1, x0 = divmod(x, 10**m)
    y1, y0 = divmod(y, 10**m)
    z0 = karatsuba(x0, y0)
    z2 = karatsuba(x1, y1)
    z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0
    return z2 * 10**(2*m) + z1 * 10**m + z0
x = 1234
y = 5678
print(karatsuba(x, y))  # Output: 7006652
