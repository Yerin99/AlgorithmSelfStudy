n = int(input())
a = list(map(int, input().split()))
lis_list = [1]
reverse_lis_list = [1]
b = a[::-1]

for i in range(1, n):
    lis = 1
    for j in range(i):
        if a[j] < a[i]:
            lis = max(lis, lis_list[j] + 1)
    lis_list.append(lis)

for i in range(1, n):
    lis = 1
    for j in range(i):
        if b[j] < b[i]:
            lis = max(lis, reverse_lis_list[j] + 1)
    reverse_lis_list.append(lis)

reverse_lis_list.reverse()

max_length = 0

for i in range(n):
    max_length = max(max_length, lis_list[i] + reverse_lis_list[i] - 1)

print(max_length)
