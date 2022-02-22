n = int(input())
divisors = sorted(list(map(int, input().split())))
print(divisors[0]*divisors[-1])
