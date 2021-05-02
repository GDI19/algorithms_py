# высисление фибоначчи только положительных чисел

import timeit
import cProfile


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(timeit.timeit('fib(3)', number=1000, globals=globals()))  # 0.0014677000000000023
print(timeit.timeit('fib(5)', number=1000, globals=globals()))  # 0.005236499999999991
print(timeit.timeit('fib(7)', number=1000, globals=globals()))  # 0.012410799999999986
print(timeit.timeit('fib(9)', number=1000, globals=globals()))  # 0.03461439999999999
print(timeit.timeit('fib(11)', number=1000, globals=globals()))  # 0.07759170000000001
# print(timeit.timeit('fib(13)', number=1000, globals=globals())) # 0.2919252
# print(timeit.timeit('fib(15)', number=1000, globals=globals())) # 0.544614

cProfile.run('fib(7)')
"""
44 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     41/1    0.000    0.000    0.000    0.000 task_1.py:4(fib)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# --------------------------------------------------------------------------------------------
def memo(func):
    def memorize(n, memory={}):
        val = memory.get(n)
        if val is None:
            val = func(n)
            memory[n] = val
        return val

    return memorize


@memo
def fib_1(n):
    if n < 2:
        return n
    return fib_1(n - 1) + fib_1(n - 2)


print(timeit.timeit('fib_1(3)', number=1000, globals=globals()))  # 0.00042730000000001933
print(timeit.timeit('fib_1(5)', number=1000, globals=globals()))  # 0.0004533000000000176
print(timeit.timeit('fib_1(7)', number=1000, globals=globals()))  # 0.0005462999999999996
print(timeit.timeit('fib_1(9)', number=1000, globals=globals()))  # 0.00045560000000000045
print(timeit.timeit('fib_1(11)', number=1000, globals=globals()))  # 0.0006106999999999918
print(timeit.timeit('fib_1(13)', number=1000, globals=globals()))  # 0.0004653000000000018
print(timeit.timeit('fib_1(15)', number=1000, globals=globals()))  # 0.0004693999999999532

cProfile.run('fib_1(20)')
"""
30 function calls (16 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     11/1    0.000    0.000    0.000    0.000 task_1.py:31(memorize)
      5/1    0.000    0.000    0.000    0.000 task_1.py:39(fib_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       11    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
"""


# -------------------------------------------------------------------------------------
def memo_2(func):
    def memorize(n, memory={0: 0, 1: 1}):
        val = memory.get(n)
        if val is None:
            val = func(n)
            memory[n] = val
        return val

    return memorize


@memo_2
def fib_2(n):
    return fib_1(n - 1) + fib_1(n - 2)


print(timeit.timeit('fib_2(3)', number=1000, globals=globals()))  # 0.0003930999999999796
print(timeit.timeit('fib_2(5)', number=1000, globals=globals()))  # 0.0004663000000000306
print(timeit.timeit('fib_2(7)', number=1000, globals=globals()))  # 0.0004463000000000106
print(timeit.timeit('fib_2(9)', number=1000, globals=globals()))  # 0.00046709999999999807
print(timeit.timeit('fib_2(11)', number=1000, globals=globals()))  # 0.0004561000000000148

cProfile.run('fib_2(20)')
"""
10 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 task_1.py:31(memorize)
        1    0.000    0.000    0.000    0.000 task_1.py:69(memorize)
        1    0.000    0.000    0.000    0.000 task_1.py:77(fib_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
"""


# --------------------------------------------------------------------------------
def fib_3(n, memo=[0, 1]):
    if n < len(memo):
        return memo[n]
    else:
        val = fib_3(n - 1) + fib_3(n - 2)
        memo.append(val)
        return val


print(timeit.timeit('fib_3(3)', number=1000, globals=globals()))  # 0.0004181999999999797
print(timeit.timeit('fib_3(5)', number=1000, globals=globals()))  # 0.0003674000000000177
print(timeit.timeit('fib_3(7)', number=1000, globals=globals()))  # 0.0003495000000000026
print(timeit.timeit('fib_3(9)', number=1000, globals=globals()))  # 0.00037840000000000096
print(timeit.timeit('fib_3(11)', number=1000, globals=globals()))  # 0.0003570999999999991

cProfile.run('fib_3(20)')

"""
50 function calls (32 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     19/1    0.000    0.000    0.000    0.000 task_1.py:107(fib_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       19    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# ----------------------------------------------------------------------------------

def fib_no_recursion(n):
    if n < 2:
        return n
    p1 = 0
    p2 = 1
    for i in range(n - 1):
        p1, p2 = p2, p1 + p2
    return p2


print(timeit.timeit('fib_no_recursion(3)', number=1000, globals=globals()))  # 0.0012398999999999605
print(timeit.timeit('fib_no_recursion(5)', number=1000, globals=globals()))  # 0.001283499999999993
print(timeit.timeit('fib_no_recursion(7)', number=1000, globals=globals()))  # 0.001573099999999994
print(timeit.timeit('fib_no_recursion(9)', number=1000, globals=globals()))  # 0.001573099999999994
print(timeit.timeit('fib_no_recursion(11)', number=1000, globals=globals()))  # 0.0018367000000000244

cProfile.run('fib_no_recursion(20)')

"""
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1.py:139(fib_no_recursion)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
def fib_4(n, memory={0: 0, 1: 1}):
    val = memory.get(n)
    if val is None:
        pp = 0
        p = 1
        for i in range(n - 1):
            pp, p = p, pp + p
        memory[n] = p
        return p
    return val

print(timeit.timeit('fib_4(3)', number=1000, globals=globals()))  # 0.
print(timeit.timeit('fib_4(5)', number=1000, globals=globals()))  # 0.
print(timeit.timeit('fib_4(7)', number=1000, globals=globals()))  # 0.
print(timeit.timeit('fib_4(9)', number=1000, globals=globals()))  # 0.
print(timeit.timeit('fib_4(11)', number=1000, globals=globals()))  # 0.
print(timeit.timeit('fib_4(9)', number=1000, globals=globals()))
print(timeit.timeit('fib_4(15)', number=1000, globals=globals()))
print(timeit.timeit('fib_4(19)', number=1000, globals=globals()))
print(timeit.timeit('fib_4(9)', number=1000, globals=globals()))
print(timeit.timeit('fib_4(9)', number=1000, globals=globals()))

cProfile.run('fib_4(20)')