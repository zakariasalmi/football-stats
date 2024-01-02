import cv2
import time

def getVideoSource(args):
	"""Get the video source based on CLI inpout arguments provided.

	Args:
		args (dict): Input arguments.

	Returns:
		VideoCapture object

	"""
	# if the video argument is None, then read from webcam
	if args.get("video", None) is None:
		video = cv2.VideoCapture(0)
		#time.sleep(0.25)

	# otherwise read from a video file
	else:
		video = cv2.VideoCapture(args["video"])

	return video