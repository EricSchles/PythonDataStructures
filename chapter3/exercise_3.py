def three_lines():
    new_line()
    new_line()
    new_line()

def new_line():
    print

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
clear_screen()
"""
After I moved new_line before three_lines I ran the program.  Everything ran fine since python was aware of both definitions when the functions were called.  This tells us that functions need not be written in order, simply before they are called.  In the program, new_line is defined before it is called, so it's fine.  When three_lines is called it simply looks for a definition of new_line, which it finds because new_line was defined before the call to three_lines.
"""
