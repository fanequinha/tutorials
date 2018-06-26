#!/usr/bin/env python

import cv2
import numpy as np
import os
import random
import tempfile

from enum import Enum
from subprocess import call

WIDTH = 640
HEIGHT = 480

class Shape(Enum):
    LINE = 1
    CIRCLE = 2
    ELLIPSE = 3
    POLYGON = 4

def shape():
    return random.choice(list(Shape))

def screenshot(img):
    dirname = tempfile._get_default_tempdir()
    filename = next(tempfile._get_candidate_names()) + '.png'
    filename = dirname + '/' + filename
    print('Screenshot %s' % filename)
    cv2.imwrite(filename, img)

def download(url, path):
    print("Downloading video: %s" % url)
    if not os.path.exists(os.path.dirname(video)):
        os.mkdir(os.path.dirname(video))
    call(["youtube-dl", url, "-o", video])
    print("Video saved: %s" % video)

def draw_shape(frame, kind):
    if kind == Shape.LINE:
        cv2.line(frame, (0,0), (WIDTH, HEIGHT), (255, 0, 0), 4)
    elif kind == Shape.CIRCLE:
        cv2.circle(frame, (WIDTH/2,HEIGHT/2), HEIGHT/2, (255, 0, 0), 4)
    elif kind == Shape.ELLIPSE:
        cv2.ellipse(frame, (WIDTH/2,HEIGHT/2), (WIDTH/2,HEIGHT/2), 0, 0, WIDTH, HEIGHT, 4)
    elif kind == Shape.POLYGON:
        pts = np.array([[WIDTH/2, 0], [WIDTH, HEIGHT/3], [WIDTH-WIDTH/5, HEIGHT], [WIDTH/5, HEIGHT], [0, HEIGHT/3]], np.int32)
        cv2.polylines(frame, [pts], True, (255, 0, 0), 4)
    else:
        raise Exception('Unknown shape: %s' % s)

def put_text(frame, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    size = 4
    thick = 4
    color = (64, 192, 255)
    cv2.putText(frame, "Fanequinha", (WIDTH/2-150,HEIGHT/2+200), 1, size, color, thick, cv2.LINE_AA)

video = 'data/spain-vs-germany-2008.mp4'
if not os.path.exists(video):
    url = "https://www.youtube.com/watch?v=qRLbzpy1y8Y"
    download(url, video)
cap = cv2.VideoCapture(video)

kind = shape()

while (True):
    # Capture frame-by-frame.
    success, frame = cap.read()

    # Our operations on the frame come here. 
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
 
    # Draw shape (line, circle, ellipse).
    draw_shape(frame, kind)

    # Put text.
    put_text(frame, 'OpenCV')

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
