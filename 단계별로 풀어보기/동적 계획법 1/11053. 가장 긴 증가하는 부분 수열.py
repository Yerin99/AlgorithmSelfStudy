n = int(input())
a = list(map(int, input().split()))
lis_list = [1]

for i in range(1, n):
    lis = 1
    for j in range(i):
        if a[j] < a[i]:
            lis = max(lis, lis_list[j] + 1)
    lis_list.append(lis)

print(max(lis_list))
