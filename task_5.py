start = 32
end = 127
step = 10

while start < 127:
    if start == 122:
        step = 6

    result = ''
    for i in range(start, start + step):
        result = result + str(i) + ' | ' + chr(i) + ' | '

    start = start + step
    print(result)
    # print('-' * len(result))
