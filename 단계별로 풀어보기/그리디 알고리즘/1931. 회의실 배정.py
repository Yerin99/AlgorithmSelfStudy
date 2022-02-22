n = int(input())
meetings = []

for _ in range(n):
    start, finish = map(int, input().split())
    meetings.append([start, finish])

meetings.sort(key=lambda meeting: (meeting[1], meeting[0]))

able_meetings = [meetings[0]]

for i in range(1, n):
    finish_prev = able_meetings[-1][1]
    start, finish = meetings[i]

    if start >= finish_prev:
        able_meetings.append(meetings[i])

print(len(able_meetings))
