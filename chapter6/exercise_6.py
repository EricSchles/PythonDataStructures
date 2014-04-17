import math
def is_prime(n):
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    """
    sqrt_n = int(math.sqrt(n))
    if n == 1:
        return False
    i = 2
    while i <= sqrt_n:
        if n%i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
