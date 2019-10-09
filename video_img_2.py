"""
Purpose: Taking a video file and saving each of the video as images, capturing
         1 frame/secondself.

Arguments: Takes in the path to the video being uploaded.

Purpose: Uses OpenCV library to read in the video and save .jpg files of the video frames every 1 second.

Notes:
    This script will take the name of the video, create a new folder on the same folder level as the video
    to save the jpg. If that folder exists then it will remove that folder and replace it with a new one.

"""

import cv2
import os
import math
import shutil
# function to capture frame.

def captureFrame(vid_path):

    #get the base directory path
    base_dir = os.path.dirname(vid_path)

    # Get the name of the video.
    video_name = vid_path.split('/')[-1].split('.')[0]
    folder_name = video_name + '_images'
    save_folder_name = os.path.join(base_dir,folder_name)

    if os.path.isdir(save_folder_name):
        shutil.rmtree(save_folder_name)
        print('The old folder has been removed\n')
        os.mkdir(save_folder_name)
    else:
        os.mkdir(save_folder_name)
        print('\nThe Folder for saving images has been created')

    print('\nSave Folder name: ', save_folder_name)

    #path to video file.
    vid_obj = cv2.VideoCapture(vid_path)
    frameRate = vid_obj.get(5)
    count = 0
    while (vid_obj.isOpened()):
        frameId = vid_obj.get(1)
        ret, frame = vid_obj.read()

        if (ret != True):
            break
        if (frameId % math.floor(frameRate) ==0):
            img_name = 'frame' + str(int(count)) + '.jpg'
            cv2.imwrite(os.path.join(base_dir,save_folder_name, img_name), frame)
            count += 1

    vid_obj.release()
    print("Done")
if __name__ == '__main__':

    captureFrame('Path to the video goes here!!')
