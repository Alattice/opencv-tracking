############################################
# separate thread that manages window updates
# python 3.6.9
#
############################################ 

import threading
import queue
import cv2
import numpy as np

class window_process(threading.Thread):
	def __init__(self, camera_port=0):
		threading.Thread.__init__(self)
		self.win_obj = cv2.VideoCapture(camera_port)

		#Check whether user selected camera is opened successfully.
		if not (self.win_obj.isOpened()):
			print("Could not open video device")
			return 1

		#To set the resolution
		self.win_obj.set(cv2.CAP_PROP_FRAME_WIDTH,640);
		self.win_obj.set(cv2.CAP_PROP_FRAME_HEIGHT,480);


	# update window
	def update(self, window): #update the window
		cv2.imshow("stream",window)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	def __exit__(self):
		# When everything done, release the capture
		self.win_obj.release()
		cv2.destroyAllWindows()