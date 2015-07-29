#!/usr/bin/env python
from math import sqrt

animals = ['cat', 'dog', 'monkey']
for animal in animals:
	print animal


# for List
nums = [0, 1, 2, 3, 4]
square = []
for num in nums:
	square.append( num ** 2 )
print square

## learn this type of assignment in the [ ]
even_squares = [ num ** 2 for num in nums if num % 2 == 0 ]
print even_squares

## dictionary is similar to the Map(Key:Value)
d = {'cat':'cute', 'dog':'furry'}
print d['cat']
print 'cat' in d	# check whether there is a key in the dictionary
d['fish'] = 'wet'
print d['fish']

print d.get('monkey', 'N/A')	# get an element with a default N/A
print d.get('fish', 'N/A')
del d['fish']
print d.get('fish', 'N/A')


## some examples about dictionary and for loop
for animal in d:
	value = d[animal]
	print animal + ": " + value

## use iteritems to get the key and value NOTE!!!!
d = {'person':2, 'cat':4, 'spider':8}
for animal, leg in d.iteritems():
	print "%s has %d legs" % (animal, leg)


nums = [1, 2, 3, 4, 5]
square_pair = {x: x ** 2 for x in nums if x % 2 == 0}
print square_pair


### Sets
animals = {'cat', 'dog'}
print 'cat' in animals
print 'fog' in animals
animals.add('fish')
print 'fish' in animals
print len(animals)
animals.add('cat')
print animals
animals.remove('cat')
print animals

## list the elements of Sets
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
	print "$%d: %s" % (idx+1, animal)

### construct the Sets
nums = {int(sqrt(x)) for x in range(30)} # Sets will avoid the repeated numbers
print nums

### Tuple: value cannot be changed
d = {(x, x+1): x for x in range(10)}
print d
t = (5, 6)
print type(t)
print d[t]
print d[(1, 2)]

