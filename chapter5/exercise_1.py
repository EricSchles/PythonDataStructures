def compare(a,b):
    """
    >>> compare(5,4)
    1
    >>> compare(7,7)
    0
    >>> compare(2,3)
    -1
    >>> compare(42,1)
    1
    """

    if a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0
    else:
        return "no comparison operator for types"+str(type(a))+" "+str(type(b))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
