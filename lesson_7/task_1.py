from random import randint

array = [randint(-100, 100) for i in range(0, 10)]
print(array)
"""
def bubble_sort(lst):
    n = 1
    while n <= len(lst):
        count = False
        for i in range(len(lst)-n):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                count = True
        if count == False:
            return lst
        n += 1
    return lst
print(bubble_sort(array))
"""


def bubble_reversed_sort(lst):
    n = 1
    while n <= len(lst):
        count = False
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count = True
        if count == False:
            return lst
        n += 1
    return lst


print(bubble_reversed_sort(array))
