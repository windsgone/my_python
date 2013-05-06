from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()

'''
from sys import argv

script = argv

print "Type the name of the file: " 
filename = raw_input()
txt = open(filename)
print txt.read()
txt.close()
'''

