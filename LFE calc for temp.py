# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:55:55 2021

@author: soura
"""

import numpy as np
import cv2
import imutils
import matplotlib.pyplot as plt
import pandas as pd


path='D:/Drone Photos/Pilot Album (1)/20210410_115120_R.jpg'
filepath='C:/Users/soura/Downloads/thermal.csv'
data = pd.read_csv(filepath,engine='python',header=None)
temp=data.to_numpy()

bottom=temp[256:512,:]
bottom = bottom.astype(float)
plt.imshow(bottom)

image = cv2.imread(path)
image=image[256:512,:]

temp_range = cv2.inRange(bottom, 58, 68)
contours,heir= cv2.findContours(temp_range, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0,0,0), 3)
cv2.imshow('Cont',image)
    
cnt = contours[0]
M = cv2.moments(cnt)
if cv2.contourArea(cnt)>50000:

    x,y,w,h = cv2.boundingRect(cnt)
    print(x,y,w,h)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.drawContours(image,[box],0,(0,0,255),2)
    cropped=image[y:y+h,x:x+w]

    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    print(box)
    cv2.drawContours(image,[box],0,(0,0,255),2)
    cv2.drawContours(image, contours, -1, (0, 0, 0), 3)
    cv2.imshow("Color",image)