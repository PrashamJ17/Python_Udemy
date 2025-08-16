def multiplier(n):
    def inner(x):
        return x * n
    return inner

times2 = multiplier(2)
times5 = multiplier(5)

print(times2(10))  # Output: 20
print(times5(10))  # Output: 50
