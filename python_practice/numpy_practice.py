#!/usr/bin/env python
"""
__author__ = , 7/14/16
"""

import os
import sys
from os import path

import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

points = np.arange(-5,5,0.01)  # 1000 points, equally spaced

# print points

xs, ys = np.meshgrid(points, points)

# print ys
# print xs

z = np.sqrt(xs ** 2 + ys ** 2)

# print z

plt.imshow(z, cmap=plt.gray())

plt.colorbar()

plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

num = 1

if path.exists(path.join('fig%s.png' % num)):

    num += 1

    plt.savefig('fig%s' % num)

path_to_nii = path.join('datasets', 'example.nii')

nii_loaded = nib.load(path_to_nii)

print nii_loaded.shape

#
print nii_loaded.get_data_dtype() == np.dtype(np.int16)

# NOW CONVERT np array to image

array_data = z

print array_data.shape

affine = np.diag([1, 1, 3, 1])

array_img = nib.Nifti1Image(z, affine)

array_img.to_filename('my_array_image.nii')
