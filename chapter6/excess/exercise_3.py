"""
def print_multiples(n, high):
    i = 1
    while i <= high:
        print n*i, '\t',
        i += 1
    print

def print_mult_table(high):
    i = 1
    while i <= high:
        print_multiples(i, high)
        i += 1

The goal is to understand print_mult_table.  So, high is the highest number whose multiples will be printed.  The value high is passed into print_multiples so that you are ensured the table will be square.  This is because high serves as an upper bound on the number of values that will be printed as well as the number of times that number is printed.  It is a good idea to steal some terminology from linear algebra here.  High acts both as the row as well as the column upper bound.  The number of rows are the number values peer column. For instance, the following table has 2 rows and 3 columns:

1 3 5 
2 4 6 

Column 1 has the values 1 and 2, column 2 has the the values 3 and 4, and column 3 has the values 5 and 6.  

If we now trace the output for say print_mult_table(3) we will have

i = 1
1    2    3

i = 2
1    2    3
2    4    6

i = 3
1    2    3
2    4    6
3    6    9

After that i = 4 which is greater than 3 so the iteration ends.
""" 
