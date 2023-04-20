total_price = int(input())
kinds = int(input())

for i in range(kinds):
    a, b = map(int, input().split())
    total_price -= a*b

if total_price == 0:
    print("Yes")
else:
    print("No")
