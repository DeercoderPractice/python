#!/usr/bin/env python
x = 3
print type(x)
print x
print x + 1
print x - 1
print x * 2
print x ** 2
x += 1
print x
x *= 2
print x
y = 2.5
print type(y)
print y, y+1, y * 2, y ** 2

# for this part I will use the boolean type of python
t= True
f = False
print type(t)
print t and f
print t or f
print not t
print t != f


# for this part, I will use the string of python
hello  = 'hello'
world = 'world'
print hello
print len(hello)
hw = hello + '  ' + world
print hw
hw12 = '%s %s %d' % (hello, world, 12)
print hw12

# string's method
s = "hello"
print s.capitalize()
print s.upper()
print s.rjust(7)	# right adjust to the 7 characters
print s.ljust(7)
print s.center(7)
print s.replace('l', '(cell)')
print '  world '.strip()  # strip the leading and trailing space

