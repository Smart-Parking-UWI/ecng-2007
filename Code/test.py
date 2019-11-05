import json
import cv2
import numpy
import ParkingAssistUtils

def driver():
    ParkingAssistUtils.regionSelection(cv2.imread('img.jpg',1))
    stuff=ParkingAssistUtils.sampleImage('vid.mp4',4)
    cv2.imshow('frame',stuff[0])
    cv2.imshow('frame1',stuff[1])
    cv2.imshow('frame2',stuff[2])
    cv2.imshow('frame3',stuff[3])
    cv2.imshow('frame4',stuff[4])
    return

driver()
