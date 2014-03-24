def insist_number(x):
    for i in x:
        if type(i) != type(int()) and type(i) != type(float()):
            return False
    return True

def c2f(t):
    """
    >>> c2f(0)
    32
    >>> c2f(100)
    212
    >>> c2f(-40)
    -40
    >>> c2f(12)
    54
    >>> c2f(18)
    64
    >>> c2f(-48)
    -54
    """
    if insist_number([t]):
       fahrenheit = t * 9.0/5 + 32
       fahrenheit = int(round(fahrenheit))
       return fahrenheit
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()

