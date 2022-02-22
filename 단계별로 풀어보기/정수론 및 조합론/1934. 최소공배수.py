T = int(input())

for i in range(T):
    A, B = sorted(map(int, input().split()))
    a, b = A, B
    while b % a != 0:
        b, a = a, b % a

    print((A*B)//a)
