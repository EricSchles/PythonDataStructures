def is_divisible_by_n(x,n):
    if type(x) == type(int()) and type(n)==type(int()):
        if x % n == 0:
            print "yes,"+str(x)+" is divisible by "+ str(n)
        else:
            print "no,"+str(x)+" is not divisible by "+str(n)
    else:
        print "invalid input"

num1 = input("Please input a number to check:")
num2 = input("Please input a divisor to check:")
is_divisible_by_n(num1,num2)
