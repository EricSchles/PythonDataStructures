def insist_number(x):
    for i in x:
        if type(i) != type(int()) and type(i) != type(float()):
            return False
    return True

def slope(x1,y1,x2,y2):
    """
    >>> slope(5,3,4,2)
    1.0
    >>> slope(1,2,3,2)
    0.0
    >>> slope(1,2,3,3)
    0.5
    >>> slope(2,4,1,2)
    2.0
    """
    if insist_number([x1,x2,y1,y2]):
        x_delta = x2-x1
        y_delta = float(y2-y1)
        return y_delta/x_delta
    return "invalid argument specified, must be numbers!!"

def intercept(x1,y1,x2,y2):
    """
    >>> intercept(1,6,3,12)
    3.0
    >>> intercept(6,1,1,6)
    7.0
    >>> intercept(4,6,12,8)
    5.0
    """
    if insist_number([x1,y1,x2,y2]):
        alpha = slope(x1,y1,x2,y2)
        beta = y2 - (alpha*x2)
        return beta

if __name__ == '__main__':
    import doctest
    doctest.testmod()
