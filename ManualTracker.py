#!/usr/bin/env python3

import cv2
import random

# Create a MultiTracker object
#tracker = cv2.TrackerKCF_create()
tracker = cv2.legacy_MultiTracker.create()


# Open the video capture
capture = cv2.VideoCapture('La La Land low.avi')

# Read the first frame of the video
success, frame = capture.read()

# Select the objects to track by drawing bounding boxes around them
while success:
    # Show the frame
    cv2.imshow("Frame", frame)

    # Check if the user pressed 'Enter' to select the objects
    key = cv2.waitKey(1)
    if key == 13:  # 13 is the Enter key
        # Get the coordinates of the bounding boxes
        bboxes = []
        colors = []
        while True:
            bbox = cv2.selectROI("Frame", frame)
            if bbox[0] == 0 and bbox[1] == 0 and bbox[2] == 0 and bbox[3] == 0:
                break
            bboxes.append(bbox)
            colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            print("Press q to quit selecting boxes and start tracking")
            print("Press any other key to select next object")
            k = cv2.waitKey(0) & 0xFF
            if (k == 113):  # 113 is the key 'q'
                break
        # Initialize the tracker with the selected bounding boxes
        for bbox in bboxes:
            tracker.add(cv2.legacy_TrackerKCF.create(), frame, bbox)
            #tracker.init(frame, bbox)
        break
    # Read a new frame
    success, frame = capture.read()

# Start the tracking loop
while success:
    # Get the updated location of the tracked objects
    success, boxes = tracker.update(frame)

    # Draw the bounding boxes on the frame
    #for i, newbox in enumerate(boxes):
    for i,newbox in enumerate(boxes):
        p1 = (int(newbox[0]), int(newbox[1]))
        p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
        #cv2.rectangle(frame, p1, p2, color=colors[i], thickness=2)
        cv2.rectangle(frame, p1, p2, color=(255,0,0), thickness=2 )

    # Show the frame
    cv2.imshow("Frame", frame)

    # Check if the user pressed 'q' to quit
    key = cv2.waitKey(1)
    if key == 113:  # 113 is the key 'q'
        break

    # Read a new frame
    success, frame = capture.read()

# Release the capture and close all windows
capture.release()
cv2.destroyAllWindows()
