#!/usr/bin/env python

# for container like List, Set or others
xs = [3, 1, 2]
print xs, xs[2]
print xs[-1]
xs[2] = 'fool'	# List can be different type
print xs
xs.append('bar')
x = xs.pop()
print x, xs

# slicing of the List
nums = range(5)
print nums
print nums[2:4]
print nums[2:]
print nums[:]
print nums[:-1]
nums[2:4] = [8, 9]
print nums
