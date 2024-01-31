#
# The following is a python program to compress images that have been generated from other places into a video format
#

import cv2
import os

image_folder = 'images'
video_name = 'video.avi'
frame_rate = 25

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, frame_rate, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()