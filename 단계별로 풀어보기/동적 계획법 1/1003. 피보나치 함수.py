# bottom-up
MAX_NUM = 40
fibo = [[1, 0], [0, 1]]

for i in range(2, MAX_NUM+1):
    zeros = fibo[i-1][0] + fibo[i-2][0]
    ones = fibo[i-1][1] + fibo[i-2][1]
    fibo.append([zeros, ones])

T = int(input())
for i in range(T):
    print(*fibo[int(input())])
