n = int(input())
wires = []

for i in range(n):
    a, b = map(int, input().split())
    wires.append([a, b])

wires.sort(key=lambda link: link[0])

lis_list = [1]

for i in range(1, n):
    lis = 1
    for j in range(i):
        if wires[j][1] < wires[i][1]:
            lis = max(lis, lis_list[j] + 1)
    lis_list.append(lis)

minimum_removal = n - max(lis_list)
print(minimum_removal)
