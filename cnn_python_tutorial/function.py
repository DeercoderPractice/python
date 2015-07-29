#!/usr/bin/env python

def sign(x):
	if x > 0:
		return 'positive'
	elif x < 0:
		return 'negtive'
	else:
		return 'zero'

def hello(name, loud=False):
	if loud:
		print 'HELLO, %s' % name.upper()
	else:
		print 'Hello, %s!' % name

hello('Bob')
hello('Fred', loud=True)

for x in [-1, 0, 1]:
	print sign(x)


