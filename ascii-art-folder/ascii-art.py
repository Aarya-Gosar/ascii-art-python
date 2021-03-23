import numpy as np 
import cv2 
import matplotlib.pyplot as plt


value_dict = {8:'@' , 7:'#' , 6:'B' , 5:'v' , 4: '/' , 3:'a' , 2:'-' , 1:'.'}

# Getting the data for image

img = cv2.imread('face1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Making it greyscale
img = img[:,250:750]           #cropping it
img = cv2.resize(img, (60,60)) #Resizing it

img_arr = np.array(img) # Converting to arrays to get pixel values
for row in img_arr:
	s = ''
	for p in row:
		n = 0
		if p < 30:
			n = 1
		elif p < 50:
			n = 2
		elif p < 80:
			n = 3
		elif p < 120:
			n = 4
		elif p < 150:
			n = 5
		elif p < 180:
			n = 6
		elif p < 220:
			n = 7
		else: 
			n = 8
		s += value_dict[n]

	print(s)
