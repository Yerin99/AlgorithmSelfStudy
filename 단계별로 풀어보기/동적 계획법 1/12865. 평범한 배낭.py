import sys
from collections import defaultdict

sys_input = sys.stdin.readline

n, maximum_weight = map(int, sys_input().split())
datum = []
for _ in range(n):
    w, v = map(int, sys_input().split())
    datum += [[w, v]]

datum.sort(key=lambda item: (item[0], -item[1]))
value_totals = defaultdict(int)

for i in range(n):
    weight, value = datum[i]
    if weight <= maximum_weight:
        candidates = defaultdict(int)
        candidates[weight] = value
        for w, v in value_totals.items():
            weight_total = w + weight
            if weight_total <= maximum_weight:
                value_total = v + value
                candidates[weight_total] = max(candidates[weight_total], value_total)

        for w, v in candidates.items():
            value_totals[w] = max(value_totals[w], candidates[w])

max_value = 0

if value_totals:
    max_value = max(value_totals.values())

print(max_value)
