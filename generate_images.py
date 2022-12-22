
import os
import sys

# using moviepy
from moviepy.editor import *
from PIL import Image


videos_folder = "C:/user/video/"
destination_folder = "C:/user/video/destination/"

# Function to rename multiple files
def main():
    i = 0
    for filename in os.listdir(video_folder):
      my_video =str(i) + ".mp4"
      print("proccesing this video :  " + my_video)
      clip = VideoFileClip(my_video) 
      # getting only first 2 seconds 
      clip = clip.subclip(1.5, 2.5) 
      # saving a frame at 1 second 
      clip.save_frame(destination_folder + str(i) +".png", t = 1) 
      i += 1
      print ("next file :" + str(i)+".png")

# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()
