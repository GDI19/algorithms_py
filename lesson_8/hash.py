import hashlib


def rabin_karp(s):
    len_sub = [i + 1 for i in range(len(s))]
    h_list = []
    for item in len_sub:
        # h_subs = hashlib.sha1(s[:item].encode('utf-8')).hexdigest()
        for i in range(len(s)):
            h_str = hashlib.sha1(s[i:i + item].encode('utf-8')).hexdigest()
            if h_str not in h_list:
                print(s[i:i + item])
            h_list.append(h_str)


rabin_karp('abcd')