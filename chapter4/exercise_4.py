print True or False # returns True
print True and False # returns False
print not(False) and True # returns True
print True or 7 # returns True
print False or 7 # returns True
print True and 0 # returns False
print False or 8 # returns True
print "happy" and "sad" #returns True, unfortunately
print "happy" or "sad" #returns True
print "" and "sad" # returns False
print "happy" and "" # returns False

"""
The reason this returns as it does is because True or False is always True where as True and False is always False.  Because the empty string or zero is equivalent to False, the statements react the way they do above.  Also for any other int or string, the boolean value is True, which explains the rest.
"""
