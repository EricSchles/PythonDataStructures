def triangular(n):
    """
    >>> triangular(1)
    1
    >>> triangular(2)
    3
    >>> triangular(3)
    6
    >>> triangular(4)
    10
    >>> triangular(5)
    15
    """
    summa = 0
    for i in xrange(n+1):
        summa += i
    return summa

def print_triangular_numbers(n):
    i = 1
    while i <= n:
        print i, "\t",triangular(i)
        i += 1
    print

print_triangular_numbers(6)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
