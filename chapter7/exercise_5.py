
def find2(strng, ch, start):
        index = start
	while index < len(strng):
		if strng[index] == ch:
			return index
		index += 1
		return -1

def count_letters(fruit,ch):
    import string
    count = 0
    for i in xrange(len(fruit)):
        if find2(fruit,ch,start=i) != -1:
            count += 1
    return count

print count_letters("hello","l")
