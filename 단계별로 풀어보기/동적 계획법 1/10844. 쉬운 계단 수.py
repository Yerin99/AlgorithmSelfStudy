# bottom-up
N = int(input())
dp = dict()
now_unit_digit_nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
    next_unit_digit_nums = [0] * 10
    for j in range(10):
        if j != 0:
            next_unit_digit_nums[j-1] += now_unit_digit_nums[j]
        if j != 9:
            next_unit_digit_nums[j+1] += now_unit_digit_nums[j]

    now_unit_digit_nums = next_unit_digit_nums[:]

print(sum(now_unit_digit_nums) % 1000000000)
