import timeit

def sum1():
    s = 0
    for i in range(1000000):
        s += i
    return s

def sum2():
    return sum(range(100000000))

print 'For Loop Sum:', timeit.timeit(sum1, number=10)
print 'Built-in Sum:', timeit.timeit(sum2, number=10)
