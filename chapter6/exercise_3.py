def print_multiples(n, high):
    #initialize and iterator
    i = 1
    #while the iterator is less than high, print n*i and a tab
    while i <= high:
        print n*i, '\t',
        i += 1
    print #print a new line

def print_mult_table(high):
    #initialize an interator
    i = 1
    #while the iterator is less than high, do print_multiples
    while i <= high:
        print_multiples(i, high)#start from i=1 to high
        i += 1 #increment high

#print_mult_table will start on line 1 and then it will continue to print out lines of integers until it reaches high.

print print_mult_table(7)
