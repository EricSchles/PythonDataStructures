def insist_number(x):
    for i in x:
        if type(i) != type(int()) and type(i) != type(float()):
            return False
    return True

def is_multiple(composite,num):
    """
    >>> is_multiple(12,3)
    True
    >>> is_multiple(12,4)
    True
    >>> is_multiple(12,5)
    False
    >>> is_multiple(12,6)
    True
    >>> is_multiple(12,7)
    False
    """
    if insist_number([num,composite]):
        if composite % num == 0:
            return True
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()

"""
alternatively you could just copy is_factor from the last exercise and use it as is.  Simply switch the arguments in the function definition for is_multiple and you are good.
