def reverse(s):
    """
    >>> reverse('happy')
    'yppah'
    >>> reverse('Python')
    'nohtyP'
    >>> reverse("")
    ''
    >>> reverse("P")
    'P'
    """
    return s[::-1]

def mirror(s):
    """
    >>> mirror("good")
    'gooddoog'
    >>> mirror("yes")
    'yessey'
    >>> mirror('Python')
    'PythonnohtyP'
    >>> mirror("")
    ''
    >>> mirror("a")
    'aa'
    """
    reverse_s = reverse(s)
    return s + reverse_s

def remove_letter(letter, strng):
    """
    >>> remove_letter('a', 'apple')
    'pple'
    >>> remove_letter('a', 'banana')
    'bnn'
    >>> remove_letter('z', 'banana')
    'banana'
    >>> remove_letter('i', 'Mississippi')
    'Msssspp'
    """
    new_string = ""
    for i in strng:
        if i != letter:
            new_string += i
    return new_string

def is_palindrome(s):
    """
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abab')
    False
    >>> is_palindrome('tenet')
    True
    >>> is_palindrome('banana')
    False
    >>> is_palindrome('straw warts')
    True
    """
    if s == reverse(s):
        return True
    return False

def remove(sub, s):
    """
    >>> remove('an', 'banana')
    'bana'
    >>> remove('cyc', 'bicycle')
    'bile'
    >>> remove('iss', 'Mississippi')
    'Missippi'
    >>> remove('egg', 'bicycle')
    'bicycle'
    """
    if sub in s:
        start = s.find(sub)
        end = start + len(sub)
        s = s[:start] + s[end:]
    return s

def count(sub, s):
    """
    >>> count('is', 'Mississippi')
    2
    >>> count('an', 'banana')
    2
    >>> count('ana', 'banana')
    2
    >>> count('nana', 'banana')
    1
    >>> count('nanan', 'banana')
    0
    """
    count = 0
    i = 0
    while i + len(sub) <= len(s):
        if sub == s[i:len(sub)+i]:
            count += 1
        i += 1
    return count

def remove_all(sub, s):
    """
    >>> remove_all('an', 'banana')
    'ba'
    >>> remove_all('cyc', 'bicycle')
    'bile'
    >>> remove_all('iss', 'Mississippi')
    'Mippi'
    >>> remove_all('eggs', 'bicycle')
    'bicycle'
    """
    while True:
        if s.find(sub) != -1:
            s = remove(sub,s)
        else:
            break
    return s

if __name__ == '__main__':
    import doctest
    doctest.testmod()
