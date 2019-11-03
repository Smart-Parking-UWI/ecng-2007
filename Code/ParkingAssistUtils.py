"""
Author: Tyrel Cadogan
Project: encg 2007 Programming project 
"""

import json
import cv2
import numpy as np

def regionSelection(img):
    """
    Performs Region Selection and Returns region coordinates r and sample image crop
    Args:
        img - Image to which to selct region from.
    """
    region = cv2.selectROI(img)
    image_crop = getCrop(region, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return  (region, image_crop)

def getCrop(region, img):
    """
    Obtain Crop from Image
    """
    return img[int(region[1]):int(region[1]+region[3]), int(region[0]):int(region[0]+region[2])]
################################################################################
def sampleImage(VID_PATH, image_num = 1):
    """
    Grab frames from stream and output them to a list
    Args:
        VID_PATH - Video source( path to video or camera index)
        image_num - number of 
    """
    output = []
    cap = cv2.VideoCapture(VID_PATH)
    i = 0;
    while(cap.isOpened()):
        ret, frame = cap.read()
        img = frame
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output.append(img)
        i = i + 1
        if (i == image_num):
            break
    cap.release()
    return output

def countCars(output_dict, check_list = [3,4,7,6,8]):
    count = 0
    for i in range(output_dict["num_detections"]):
        if(output_dict["detection_classes"][i] in check_list and 
           (output_dict['detection_scores'][i] > .90) ):
            count +=1
    return count
                   
