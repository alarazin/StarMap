#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cv2
import matplotlib.pyplot as plt
import numpy as np 




def find_patch(image1, image2): #image1: patch, image2: starmap
  BRISK = cv2.BRISK_create()
  kp1, descriptors1 = BRISK.detectAndCompute(image1, None)
  kp2, descriptors2 = BRISK.detectAndCompute(image2, None)

  BFMatcher = cv2.BFMatcher(normType = cv2.NORM_HAMMING,
                          crossCheck = True)
  matches = BFMatcher.match(queryDescriptors = descriptors1,
                            trainDescriptors = descriptors2)
  matches = sorted(matches, key = lambda x: x.distance)

  good=matches[:11]
  MIN_MATCH_COUNT=10
  if len(good)>=MIN_MATCH_COUNT:
      src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
      dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
      M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
      matchesMask = mask.ravel().tolist()
      h,w = image1.shape
      pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
      dst = cv2.perspectiveTransform(pts,M)
      img_box = cv2.polylines(image2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

  else:
      print("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
      matchesMask = None

  draw_params = dict(matchColor = (0,255,0), 
                    singlePointColor = None,
                    matchesMask = matchesMask,
                    flags = 2)

  img_box_kp = cv2.drawMatches(image1,kp1,image2,kp2,good,None,**draw_params)
  return img_box_kp, np.int32(dst)



