#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:15:23 2020

@author: rizvi
"""

import os
import cv2
import numpy as np


inputDir = "path/to/image/directory/"
outputDir = "path/to/output/directory/"

def dilate(image_name):
    img = cv2.imread(inputDir+image_name,0)
    img = (255-img)
    
    k1 = np.ones((1,5),np.uint8)
    dst = cv2.dilate(img,k1,iterations = 5)
    
    return dst

#--------------------------------------------------------------------------
    

allFilenames = []
for (dirpath, dirnames, filenames) in os.walk(inputDir):
    allFilenames.extend(filenames)
    break

for currFile in allFilenames:    
    img_dilated = dilate(currFile)
    img = cv2.imread(inputDir+currFile,0)
    img = (255-img)
    
    # Get binary image
    _, img_bin = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    img = (255-img)
    
    # Estimate the distance transform
    dist_transform = cv2.distanceTransform(img, cv2.DIST_L2, 3)
    dist_transform = (255-dist_transform)
    
    dist2 = np.zeros((img.shape[0], img.shape[1], 3))
    
    # BGR
    dist2[:,:,0] = dist_transform
    dist2[:,:,2] = img_dilated
    dist2[:,:,1] = img_bin
    cv2.imwrite(outputDir+currFile,dist2)

print ("End reached...")
