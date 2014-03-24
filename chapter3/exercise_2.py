clear_screen()

def new_line():
    print

def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

new_line()
print "Hello"
three_lines()
print "How are you?"
nine_lines()
print "I'm fine"
"""
The error message is NameError, 'clear_screen' is not defined.  The reason this happens is because inside of main, clear_screen hasn't been defined yet.  This is because programs are executed sequentially.  Function definitions should always appear before function calls in the program since the program is always run in order from top to bottom.
"""
