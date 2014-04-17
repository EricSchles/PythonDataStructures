def num_digits(n):
    """
    >>> num_digits(12345)
    5
    >>> num_digits(0)
    1
    >>> num_digits(-12345)
    5
    >>> num_digits(2)
    1
    >>> num_digits(24)
    2
    """
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n:
        count = count + 1
        n = n / 10
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
