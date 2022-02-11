# bottom-up
MAX_NUM = 100
P = [0]*(MAX_NUM+1)
P[1] = P[2] = P[3] = 1

for i in range(4, MAX_NUM+1):
    P[i] = P[i-2] + P[i-3]

T = int(input())

for _ in range(T):
    N = int(input())
    print(P[N])
