"""
Author: Tyrel Cadogan
Project: encg 2007 Programming project 
"""

import json
import cv2
import numpy as np

import tensorflow as tf

import numpy as np
import os

from ParkingAssistUtils import * 




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
    """
    output_dict - output diction from model
    check_list - the index of the objects to count
    """
    count = 0
    
    for i in range(output_dict["num_detections"]):
        if(output_dict["detection_classes"][i] in check_list and 
           (output_dict['detection_scores'][i] > .90) ):
            count +=1
    return count

def mutlpleRegionSelector(img):
    region_list = []
    car_count_list = []
    while(1):
        print("Please Select a region")
        region, img_crop = regionSelection(img)
        car_count = input("Please Enter the number of car spaces in this region: ")
        region_list.append(region)
        car_count_list.append(car_count)
        print("Do you wish to continue?(y/n)")
        continue_check = input("Enter your input: ")
        if(continue_check =="n"): break
    return (region_list, car_count_list) 