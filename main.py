#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 02:01:41 2021

@author: alarazindancioglu
"""


import argparse
from utils import find_patch
import cv2
import os

parser=argparse.ArgumentParser()
parser.add_argument('--main_image', help='directory for big image')
parser.add_argument('--patch_image', help = 'directory for patch_image')
args=parser.parse_args()

big_img_dir = args.main_image
patch_img_dir = args.patch_image


big_img=cv2.imread(os.path.join('Images',big_img_dir), cv2.IMREAD_GRAYSCALE)
patch_img = cv2.imread(os.path.join('Images',patch_img_dir), cv2.IMREAD_GRAYSCALE)

out_img, corners = find_patch(patch_img, big_img)

cv2.imwrite(os.path.join('Output', patch_img_dir), out_img)
print("Corner points:\n", corners)