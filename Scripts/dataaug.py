import cv2
import numpy as np

j = 0 #starting number for images to be saved

for i in range(0,51): #for names of images to be read
	X = 0
	Y = 0

	val = str(i)
	extn1 = 'orig.jpg'   #extension for input images
	extn2 = 'disc.png'   #extension for disc mask
	extn3 = 'cup.png'    #extension for cup mask
	loc = ''             #base location for the images

	img = loc + val + extn1
	print(img)

	def CallBackFunc(event, x, y, flags, param):	
		global X
		global Y	
		if event == cv2.EVENT_MOUSEMOVE:
			X = x
			Y = y		
			cv2.rectangle(image, (X,Y), (X + 200, Y  + 200), (0,255,0), 2)
		

	cv2.namedWindow('original') 
	cv2.setMouseCallback('original', CallBackFunc)



	while(True):
		image = cv2.imread(img)
		while(True):
			image = cv2.imread(img)
			cv2.rectangle(image, (X,Y), (X + 200, Y  + 200), (0,255,0), 2)
			cv2.imshow('original', image)
			k = cv2.waitKey(1) & 0xFF
			if k == 27:
				break

		image = cv2.imread(img)
		cv2.destroyAllWindows()

		uh = Y
		lh = Y + 200
		lw = X
		rw = X + 200
		ch = 0
		ifs = image[uh:lh, lw:rw]
		#Saving cropped images
		ch = int(input("Enter choice (1 to save): "))
		if ch == 1:
			break
	val1 = str(j)
	img = loc + 'cr' + val1 + extn1
	cv2.imwrite(img, ifs)

	img = loc + val + extn2
	image = cv2.imread(img)
	ifs = image[uh:lh, lw:rw]
	img = loc + 'cr' + val1 + extn2
	cv2.imwrite(img, ifs)

	img = loc + val + extn3
	image = cv2.imread(img)
	img = loc + 'cr' + val1 + extn3    
	ifs = image[uh:lh, lw:rw]
	cv2.imwrite(img, ifs)
	j += 1

