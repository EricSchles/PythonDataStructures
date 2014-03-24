def insist_number(x):
    for i in x:
        if type(i) != type(int()) and type(i) != type(float()):
            return False
    return True

def is_factor(num,composite):
    """
    >>> is_factor(3,12)
    True
    >>> is_factor(5,12)
    False
    >>> is_factor(7,14)
    True
    >>> is_factor(2,14)
    True
    >>> is_factor(7,15)
    False
    """
    if insist_number([num,composite]):
        if composite % num == 0:
            return True
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
