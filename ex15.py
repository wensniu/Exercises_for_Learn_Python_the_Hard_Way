#Reading Files
from sys import argv

script, filename = argv#to get a filename

txt = open(filename)#new command open
#what you get back from open is a file

print "Here's your file %r:" % filename
# print a little message
print txt.read()

print "Tyoe the filename again:"
file_again =raw_input("> ")

txt_again =open(file_again)

print txt_again.read()
