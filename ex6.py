#strings and text
x="There are %d types of people." % 10
binary = "binary"
do_not ="don't"
y="Those who know %s and those who %s."%(binary, do_not)#1st

print x
print y

print "I said: %r." % x#2nd
print "I also said: '%s'." % y#3rd

hilarious=False
joke_evaluation="Isn't that joke so funny?! %r"#4th

print joke_evaluation % hilarious#4th

w="This is the left side of..."
e="a string with a right side."

print w+e#5th
