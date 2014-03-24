def is_divisible_by_2_or_5(n):
    """
    >>> is_divisible_by_2_or_5(8)
    True
    >>> is_divisible_by_2_or_5(7)
    False
    >>> is_divisible_by_2_or_5(5)
    True
    >>> is_divisible_by_2_or_5(9)
    False
    >>> is_divisible_by_2_or_5(27)
    False
    """
    if type(n) == type(int()):
        if n % 2 == 0 or n % 5 == 0:
            return True
        return False
    return False
            
if __name__ == '__main__':
    import doctest
    doctest.testmod()

