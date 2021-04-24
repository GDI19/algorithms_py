def recursion(a, b, step=0):
    """
    :param step:
    :param a: 1
    :param b: 4
    :return: 1, 2 , 3, 4

    :param a: 4
    :param b: 4
    :return: 4
    """
    print(f'{step=}')
    if a == b:
        return f'{a}'
    if a < b:
        rec = recursion(a + 1, b, step=step + 1)
        print(f'revert {step=} {rec=}')
        return f'{a}, {rec}'
    if a > b:
        rec = recursion(a - 1, b, step=step + 1)
        print(f'revert {step=} {rec=}')
        return f'{a}, {rec}'


if __name__ == '__main__':
    print(recursion(1, 4))
    print(recursion(3, 4))
    print(recursion(5, 4))
    print(recursion(3, 3))
