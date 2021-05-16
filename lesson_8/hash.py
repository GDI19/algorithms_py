"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных
подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
"""

import hashlib


def rabin_karp(s):
    len_sub = [i + 1 for i in range(len(s) - 1)]
    h_list = []
    count = 0
    for item in len_sub:
        h_subs = hashlib.sha1(s[:item].encode('utf-8')).hexdigest()
        for i in range(len(s)):
            h_str = hashlib.sha1(s[i:i + item].encode('utf-8')).hexdigest()
            if h_str not in h_list:
                print(s[i:i + item])
                count += 1
            h_list.append(h_str)
    return count


print(rabin_karp('sova'))