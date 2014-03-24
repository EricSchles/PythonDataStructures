def insist_number(x):
    for i in x:
        if type(i) != type(int()) and type(i) != type(float()):
            return False
    return True

def f2c(t):
    """
    >>> f2c(212)
    100
    >>> f2c(32)
    0
    >>> f2c(-40)
    -40
    >>> f2c(36)
    2
    >>> f2c(37)
    3
    >>> f2c(38)
    3
    >>> f2c(39)
    4
    """
    if insist_number([t]):
       celsius = (t - 32) * 5/9.0
       celsius = int(round(celsius))
       return celsius
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()

