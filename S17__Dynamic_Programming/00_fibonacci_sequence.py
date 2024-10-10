counter = 0
memo = [None] * 100

def fib(n):
    global counter
    counter += 1

    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)


def fib_memoization(n):
    global counter
    counter += 1
    if memo[n] is not None:
        return memo[n]

    if n == 0 or n == 1:
        return n

    memo[n] = fib_memoization(n - 1) + fib_memoization(n - 2)
    return memo[n]

def fib_bottom_up(n):
    global counter
    fib_list = [0, 1]
    for index in range(2, n+ 1):
        counter += 1
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list[n]


n = 99

print('\nFib of', n, '=', fib_bottom_up(n))
print('Number of calls to fib:', counter)
