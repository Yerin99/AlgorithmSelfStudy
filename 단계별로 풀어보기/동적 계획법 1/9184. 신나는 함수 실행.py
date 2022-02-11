def w(x, y, z):
    w_value = dp.get((x, y, z))
    if w_value is not None:
        return w_value

    if x <= 0 or y <= 0 or z <= 0:
        return 1

    elif x > 20 or y > 20 or z > 20:
        return w(20, 20, 20)

    elif x < y < z:
        dp[(x, y, z)] = w(x, y, z-1) + w(x, y-1, z-1) - w(x, y-1, z)

    else:
        dp[(x, y, z)] = w(x-1, y, z) + w(x-1, y-1, z) + w(x-1, y, z-1) - w(x-1, y-1, z-1)

    return dp[(x, y, z)]


MAX_NUM = 50
dp = dict()
w(MAX_NUM, MAX_NUM, MAX_NUM)

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
