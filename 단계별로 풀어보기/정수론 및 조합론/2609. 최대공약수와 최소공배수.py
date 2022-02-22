a, b = map(int, input().split())
gcd = 1

for i in range(2, min(a, b)+1):
    while a % i == 0 and b % i == 0:
        a //= i
        b //= i
        gcd *= i

print(gcd)
print(gcd*a*b)
