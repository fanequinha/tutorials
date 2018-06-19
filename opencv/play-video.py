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

# URL: https://www.youtube.com/watch?v=qRLbzpy1y8Y
video = 'data/spain-vs-germany-2008.mp4'
cap = cv2.VideoCapture(video)

while (True):
    # Capture frame-by-frame.
    success, frame = cap.read()

    # Our operations on the frame come here. 
    frame = cv2.resize(frame, (640, 480))

    # Display the resulting frame.
    cv2.imshow('frame', frame)

    # Actions.
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        screenshot(frame)

# When everything done, release the capture.
cap.release()
cv2.destroyAllWindows()
