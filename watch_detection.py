import cv2
import numpy as numpy

watch_cascade = cv2.CascadeClassifier('data/watch-cascade-12stages.xml')

cap = cv2.VideoCapture(0)

while (cap.isOpened()): #check !
	# capture img-by-img
	ret, img = cap.read()

	if ret: # check ! (some webcam's need a "warmup")
		#our operation on img come here
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		watches = watch_cascade.detectMultiScale(gray, 30, 30)
		
		for (x,y,w,h) in watches:
			cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)

	cv2.imshow('img', img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()				