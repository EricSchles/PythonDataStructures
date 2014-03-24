def insist_number(x):
    for i in x:
        if type(i) != type(int()) and type(i) != type(float()):
            return False
    return True

def is_even(n):
    """
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """
    if insist_number([n]):
        if n % 2 == 0:
            return True
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
