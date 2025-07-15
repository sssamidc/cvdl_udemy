#!/usr/bin/env python3

import cv2
import numpy as np

######################
## GLOBAL VARIABLES ##
######################

drawing = False

###############
## FUNCTIONS ##
###############

def draw_circle(event,x,y,flags,params):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        drawing = False
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img=pimg,center=(x,y),radius=50, color=(255,0,0), thickness=2)

#######################
## Display the image ##
#######################

# Load the image
pimg = cv2.imread("../CourseMaterial/Computer-Vision-with-Python/DATA/dog_backpack.jpg")

# Naming window and callbacks
cv2.namedWindow(winname='puppy_circle')
cv2.setMouseCallback('puppy_circle',draw_circle)

while True:
    cv2.imshow('puppy_circle',pimg)
    # Checks for hitting the `Esc` key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Close all windows when done
cv2.destroyAllWindow()