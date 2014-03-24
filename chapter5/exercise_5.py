def insist_number(x):
    for i in x:
        if type(i) != type(int()) and type(i) != type(float()):
            return False
    return True

def is_odd(n):
    """
    >>> is_odd(2)
    False
    >>> is_odd(3)
    True
    """
    if insist_number([n]):
        if n % 2 != 0:
            return True
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
