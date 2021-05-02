import timeit
import cProfile
# import random

# n = random.randint(0, 1000)
def simple_num(n):
    if n > 1:
        i = 2
        while n > i:
            if n % i == 0:
                return f'число {n} не является простым'
            else:
                i += 1
        return f'число {n} является простым'
    return f'Передано число: {n}. Отрицательные числа, так же как 0 и 1 не являются простыми'

print(timeit.timeit('simple_num(13)', number=1000, globals=globals()))   # 0.0030612
print(timeit.timeit('simple_num(71)', number=1000, globals=globals()))   # 0.016370899999999994
print(timeit.timeit('simple_num(139)', number=1000, globals=globals()))  # 0.029317899999999994
print(timeit.timeit('simple_num(223)', number=1000, globals=globals()))  # 0.0442024
print(timeit.timeit('simple_num(293)', number=1000, globals=globals()))  # 0.05756739999999999
print(timeit.timeit('simple_num(383)', number=1000, globals=globals()))  # 0.0814906
print(timeit.timeit('simple_num(995)', number=1000, globals=globals()))  # 0.0015531000000000295

cProfile.run('simple_num(997)')
"""
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 simple_num.py:6(simple_num)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# ------------------------------------------------------------------------------------------------

def eratosthene(n):
    sieve = [i for i in range(n+1)]
    sieve[1] = 0
    i = 2
    while i <= n:
        if sieve[i] != 0:
            j = i + i
            while j <= n:
                sieve[j] = 0
                j = j + i
        i = i + 1
    return sieve
print(timeit.timeit('eratosthene(13)', number=1000, globals=globals()))
print(timeit.timeit('eratosthene(71)', number=1000, globals=globals()))
print(timeit.timeit('eratosthene(139)', number=1000, globals=globals()))
print(timeit.timeit('eratosthene(223)', number=1000, globals=globals()))
print(timeit.timeit('eratosthene(294)', number=1000, globals=globals()))
"""
0.0079071
0.042820499999999984
0.09387970000000001
0.1576845
0.23227949999999997
"""

cProfile.run('eratosthene(294)')
"""
         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 simple_num.py:38(eratosthene)
        1    0.000    0.000    0.000    0.000 simple_num.py:39(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# --------------------------------------------------------------------------------------------

def geek_eratos(n):
    HOLE = 0
    sieve = [i for i in range(n+1)]
    sieve[1] = HOLE
    for i in range(2, n+1):
        if sieve[i] != HOLE:
            j = i + i
            while j <= n:
                sieve[j] = HOLE
                j += i
    return sieve

print(timeit.timeit('geek_eratos(13)', number=1000, globals=globals()))
print(timeit.timeit('geek_eratos(71)', number=1000, globals=globals()))
print(timeit.timeit('geek_eratos(139)', number=1000, globals=globals()))
print(timeit.timeit('geek_eratos(223)', number=1000, globals=globals()))
print(timeit.timeit('geek_eratos(294)', number=1000, globals=globals()))
"""
0.006899199999999994
0.08345469999999999
0.07410549999999994
0.1144714
0.16557109999999997
"""

cProfile.run('geek_eratos(294)')
"""
5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 simple_num.py:80(geek_eratos)
        1    0.000    0.000    0.000    0.000 simple_num.py:82(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""