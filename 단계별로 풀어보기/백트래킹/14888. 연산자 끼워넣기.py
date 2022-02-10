# 같은 것이 있는 순열
def get_operators(operators):
    if len(operators) == N-1:
        total = calc_total(operators)
        totals.append(total)
        return 0

    for i in range(4):
        if nums_of_operators[i] >= 1:
            nums_of_operators[i] -= 1
            get_operators(operators + [operator_dictionary[i]])
            nums_of_operators[i] += 1


def calc_total(ops):
    now_total = int(numbers[0])
    for i in range(N - 1):
        op = ops[i]
        next_num = int(numbers[i + 1])
        if op == '/':
            now_total = int(now_total / next_num)
        else:
            now_total = eval(f'{now_total}{op}{next_num}')
    return now_total


N = int(input())
numbers = input().split()
nums_of_operators = list(map(int, input().split()))

operator_dictionary = {0: '+', 1: '-', 2: '*', 3: '/'}
totals = []

get_operators([])
print(max(totals))
print(min(totals))
