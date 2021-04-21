# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:34:34 2020

@author: soura
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img=Image.open('D:/Drone Photos/10802956181610577374000.jpg')
img_array=np.array(img)
img_r=img_array[:,:,0]
img_g=img_array[:,:,1]
img_b=img_array[:,:,2]



r=img_r/(img_r + img_b + img_g)
g=img_g/(img_r + img_b + img_g)
b=img_b/(img_r + img_b + img_g)

therm=r/(r+g+b)
temp_min=5.6
temp_max=16.2
minimum=np.min(therm)
maximum=np.max(therm)

temp=temp_min+((temp_max-temp_min)*(therm-minimum)/(maximum-minimum))
temperature=18.68*therm**2+1.42*therm+5.8
tempC=temp
tempF=1.8*tempC+32
temp=temp+273
# np.savetxt('temp.csv',temp,delimiter=',')
Ts=28+273
Tin=22+273
Tm=((Ts+temp))/2
Tout=11+273
boltz=5.67*1e-8
e=0.8
h=5
v=1
temp=temperature+273

U=(4*e*boltz*Tm**3*(Ts-temp)+3.8045*v*(Ts-Tin))/(Tin-Tout)
U1=(e*boltz*(temp**4-Tout**4)+3.8045*v*(temp-Tout))/(Tin-Tout)
R1=1/U1

P=5.67*e*((temp/100)**4-(Tout/100)**4)+3.8054*v*(temp-Tout)
U2=P/(Tin-Tout)
R2=1/U2