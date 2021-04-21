# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:20:10 2020

@author: soura
"""



import numpy as np
import cv2
import imutils
import matplotlib.pyplot as plt

path='D:/Download/Py/FLIR/10802955081600883676000.jpg'
image = cv2.imread(path) # path = path to your file

#image=image[240:,100:500]
#bin = cv2.inRange(image, (130, 180, 10), (160, 190,20)
#cv2.bitwise_not(bin, bin)
#cnts = cv2.findContours(bin.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cnts = imutils.grab_contours(cnts)
#cnts = sorted(cnts, key = cv2.contourArea, reverse = True)
#rect = cv2.boundingRect(cnts[0])
#cv2.rectangle(image, rect, (0,255,0), 1)


image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#(BRG)

# def top(image):
#     image=image[120:360,:]
#     cv2.imshow('Cropped',image)
    
    
# #Color range for roof
#     lower_red = np.array([220, 40, 30])
#     upper_red = np.array([240, 140,80])
#     mask_red = cv2.inRange(image, lower_red, upper_red)
#     contours,heir= cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cv2.drawContours(image, contours, -1, (0, 0, 0), 3)
#     cv2.imshow('Cont',image)
    
#     cnt = (contours[0])
#     area = cv2.contourArea(cnt)
#     print(area)
#     #M = cv2.moments(cnt)
    
#     if cv2.contourArea(cnt)>20000:
    
#         x,y,w,h = cv2.boundingRect(cnt)
#         print(x,y,w,h)
#         cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
#         #cv2.drawContours(image,[box],0,(0,0,255),2)
#         cropped=image[y:y+h,x:x+w]
#         print (w)
#         # rect = cv2.minAreaRect(cnt)
#         # box = cv2.boxPoints(rect)
#         # box = np.int0(box)
#         # cv2.drawContours(image,[box],0,(0,0,255),2)
#         # print(box)
#         # cv2.drawContours(image,[box],0,(0,0,255),2)
#         # cv2.drawContours(image, contours, -1, (0, 0, 0), 3)
#         cv2.imshow("Color",image)
#         #cv2.imwrite("contours_green.jpg",image)
#         cv2.imshow("Cropped",cropped)

#         width=25
#         #width=float(input("Width of Building in feet:"))
#         ppf=width/w
#         return ppf

def lower(image,ppf):
    image=image[240:,400:]
    
    #Color range for roof
    lower_green = np.array([130, 140, 10])
    upper_green = np.array([160, 200,30])
    mask_green = cv2.inRange(image, lower_green, upper_green)
    contours,heir= cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 0, 0), 3)
    cv2.imshow('Cont',image)
    cnt = contours[0]
    M = cv2.moments(cnt)
    if cv2.contourArea(cnt)>700:
    
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
        #cv2.imwrite("contours_green.jpg",image)
        #cv2.imshow("Cropped",cropped)


        
       
    
        height=h*ppf*12
        return height
    
        

PPF=lower(image)
# Height=lower(image,PPF)
# print("Calculated Height:",Height,"inches")
cv2.imwrite("Box.jpg",image)
cv2.waitKey(0)