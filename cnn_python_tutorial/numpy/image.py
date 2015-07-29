#!/usr/bin/env python

from scipy.misc import imread, imsave, imresize, imshow

img = imread('vim.png')
print img.dtype, img.shape

img_tinted = img * [1, 0.95, 0.9, 0.9] # here we multiply by 4-dim instead of 3-dim as it has 4 for svg images
img_tinted = imresize(img_tinted, (300, 300))

imsave('vim_tinted.png', img_tinted)
imshow(img)
imshow(img_tinted)
