#!/usr/bin/env python

import numpy as np
import cv2
import os
import tempfile

def screenshot(img):
    dirname = tempfile._get_default_tempdir()
    filename = next(tempfile._get_candidate_names()) + '.png'
    filename = dirname + '/' + filename
    print('Screenshot %s' % filename)
    cv2.imwrite(filename, img)

cap = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame.
    ret, frame = cap.read()

    # Our operations on the frame come here. 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame.
    cv2.imshow('frame', gray)

    # Actions.
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        screenshot(gray)

# When everything done, release the capture.
cap.release()
cv2.destroyAllWindows()
