#Prompting and Passing
from sys import argv

Script, user_name = argv
#prompt='> '
prompt="> "
#prompt='* '

print "Hi %s, I'm the %s script." % (user_name,Script)
print "I'd like to ask you a few questions."
print "Do youlike me %s?" %user_name
likes=raw_input(prompt)

print "Where do you live %s?" % user_name
lives=raw_input(prompt)

print "What kind of computer do you have?"
computer=raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

#python ex14.py wensen
