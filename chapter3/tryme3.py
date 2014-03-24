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
clear_screen()
