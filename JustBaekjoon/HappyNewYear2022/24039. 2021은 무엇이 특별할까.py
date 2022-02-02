N = int(input())

# 10000보다 큰 특별한 수 중에
# 가장 작은 특별한 수를 만드는 두 수는
# 101과 103

MAX_PRIME = 103
numbers = [True]*(MAX_PRIME+1)
primes = []

# 에라토스테네스의 체

for i in range(2, MAX_PRIME+1):
    if numbers[i]:
        primes.append(i)
        for j in range(2*i, MAX_PRIME+1, i):
            numbers[j] = False

for i in range(len(primes)):
    special_number = primes[i] * primes[i+1]
    if special_number > N:
        print(special_number)
        break
